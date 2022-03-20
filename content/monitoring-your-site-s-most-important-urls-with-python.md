Title: Monitoring your site's most important URLs with Python
Date: 2022-03-19 15:09
Category: Python
Tags: Search Console API, cron, requests
Author: Freddie Larkins
Summary: I wrote a few Python scripts that monitor your site's most important URLs for any 4xx and 5xx errors. Here's how they work.
Slug: monitoring-your-site-s-most-important-urls-with-python

**I've you've ever discovered a piece of content has been accidentally redirected or removed, this article might be for you.**

As SEOs, we're precious about our site's traffic - especially when we're losing it! The inspo for this collection of Python scripts arose at work, where I'd noticed a few pieces of traffic-driving bits of content had been accidentally redirected elsewhere, or were stuck in infinite redirect loops. Of course, in both cases, traffic loss was the result.

This [GitHub repo was](https://github.com/fredlarkins/monitor-top-urls) my attempt to set up an automated monitoring system for a site's top URLs by organic clicks, checking daily for 4xx and 5xx errors and emailing you the results of the check. If you just want to go ahead and try it, run:
```
git clone https://github.com/fredlarkins/monitor-top-urls.git
```
... and follow the README.md for set-up instructions.

Otherwise, here's how it works in a little more detail.

## Querying the Search Console API
The idea behind this project was to only monitor the site's most important URLs for downtime. Therefore, the script queries the Search Console API (GSC API) for a list of the top X URLs (where X is specified by the user when invoking the script) by organic clicks.

The `query()` function in `query_search_console.py` does this job. Using Josh Carty's user-friendly [google-searchconsole](https://github.com/joshcarty/google-searchconsole) package, it authenticates to the API with client_secret.json and client_config.json files - downloaded from the Google Develeoper Console. The important bit of the function is this:
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

Calling `query()` supplies us with the list of URLs that are checked for errors.

