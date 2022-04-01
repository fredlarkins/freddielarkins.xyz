Title: Monitoring your site's most important URLs with Python
Date: 2022-03-19 15:09
Category: Python
Tags: Search Console API, aiohttp, yagmail
Author: Freddie Larkins
Summary: I wrote a few Python scripts that monitor your site's most important URLs for any 4xx and 5xx errors. Here's how they work.
Slug: monitoring-your-site-s-most-important-urls-with-python

**I've you've ever discovered a piece of content has been accidentally redirected or removed, this article might be for you.**

As SEOs, we're precious about our site's traffic - especially when we're losing it! The inspo for this collection of Python scripts arose at work, where I'd noticed a few pieces of traffic-driving bits of content had been accidentally redirected elsewhere, or were stuck in infinite redirect loops. Of course, in both cases, traffic loss was the result.

This [GitHub repo was](https://github.com/fredlarkins/monitor-top-urls) my attempt to set up an automated monitoring system for a site's top URLs by organic clicks, checking daily for 4xx and 5xx errors and emailing you the results of the check.

<div class="github-card" data-github="fredlarkins/monitor-top-urls" data-width="400" data-height="" data-theme="default"></div>
<script src="//cdn.jsdelivr.net/github-cards/latest/widget.js"></script>

If you just want to go ahead and try it, run:
```
git clone https://github.com/fredlarkins/monitor-top-urls.git
```
... and follow the README.md for set-up instructions.

Otherwise, here's how it works in a little more detail.

## Querying the Search Console API
The idea behind this project was to only monitor the site's most important URLs for downtime. Therefore, the script queries the Search Console API (GSC API) for a list of the top X URLs (where X is specified by the user when invoking the script) by organic clicks.

The `query()` function in `query_search_console.py` does this job. Using Josh Carty's user-friendly [google-searchconsole](https://github.com/joshcarty/google-searchconsole) package, it authenticates to the API with client_secret.json and client_config.json files - downloaded from the Google Developer Console. The important bit of the function is this:
```python

df = webprop.query\ # webprop is a 'webproperty' object - just like the properties you see in the GSC GUI
        
        # asks the API for the last month of data
        .range(start='today', months=-1)\

        # aggregates the data by page
        .dimension('page')\

        # limits the number of URLs returned by the API to num_urls...
        # ... which is supplied by the user as a command-line argument
        .limit(num_urls)\

        .get()\
        .to_dataframe()

return df # return the result as a DataFrame
```

Calling `query()` supplies us with the DataFrame from which we'll get the list of URLs that are checked for errors.

## Checking the URLs for errors
The `check_urls.py` takes care of this part, leveraging the aiohttp library. For an awesome video on using aiohttp to make requests, check out John Watson Rooney's ['Web Scraping with AIOHTTP and Python'](https://youtu.be/lUwZ9rS0SeM).

There are two really cool things about aiohttp. First, you can make requests asynchronously. aiohttp won't wait for the response from URL X before it requests URL Y - radically speeding up how many requests you can make in a given time period.

Second, when you call `session.get(url)` using an `aiohttpClientSession` object, only the response headers are returned, rather than the full HTML contents. The latter can be obtained via the `text()` method. It's a lightweight way of getting the information we need; after all, if we only want to know whether the URL is throwing an error or has been redirected, we only need the response codes from the server.

Expressed in code, it looks like this:
```python
 async with session.get(url) as resp:
        status_code = int(resp.status)
        resolved_url = resp.url
        error_message = None
        if resp.history:
                redirect_type = int(resp.history[-1].status)
                redirect_url = resp.history[-1].url
        else:
                redirect_type = 0
                redirect_url = None
```
Notice we're not calling `resp.text()` at any point, as we don't need the HTML content to ascertain whether the URL is returning a 3xx or 4xx status code.

Looping through each of the URLs obtained in the previous step, we'll record the URL, status code, error message (if applicable, e.g. in the case of a server error), redirect type, redirect URL and resolved URL. If any URLs throw errors, the user will be emailed in the next step.

## Emailing the user about errors
`app.py` is where all the scripts are brought together. It uses the argparse library to take command-line arguments like the number of URLs to check and the recipients of the warning emails. It then runs through the flow outlined above, and uses a bit of conditional logic to send one of two email templates to the recipient: Errors Discovered, or No New Errors discovered.
![Screenshot of a warning email](/images/png/errors-detected.png)
<center>_Oh no!_</center>

The emails are sent using the [yagmail](https://pypi.org/project/yagmail/) package, a wonderfully simple SMTP client. Sadly, Gmail are retiring the option to allow less-secure-app-access to a Google account in summer '22; thereafter, sending emails via yagmail will require (I assume) some sort of OAuth implementation. So enjoy it while it lasts!

## Learnings
This was the first repo I made public on my GitHub, so it was quite exciting to release. I'm under no illusions that nobody will really use it, but it's a useful exercise to pretend as though people will! That forces you to focus on catching errors and communicating to the user why the script failed.

Having said that, reading back through my code was a bit of a challenge. It's rather unwieldy and the end result could probably be achieved in one python file rather than several. It would also have been cool to have integrated a means of keeping track of _known_ errors. I noticed that it would remind me every day of the same problem URLs.

Overall, though, I'm proud of it as my first attempt to give back to the SEO Pythonista community. 3 GitHub stars and counting!