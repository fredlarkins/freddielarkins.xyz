# Random stuff that I may find useful down the line

## Custom 404 pages
From the [tips.rst](https://github.com/getpelican/pelican/blob/master/docs/tips.rst) file in Pelican docs:

>When a browser requests a resource that the web server cannot find, the web server usually displays a generic "File not found" (404) error page that can be stark and unsightly. One way to provide an error page that matches the theme of your site is to create a custom 404 page (not an article), such as this Markdown-formatted example stored in content/pages/404.md:
>```
>Title: Not Found
>Status: hidden
>Save_as: 404.html
>
>The requested item could not be located. Perhaps you might want to check the [Archives](/archives.html)?
>```

And then configuring Apache to show this error page:
>```
>ErrorDocument 404 /404.html
>```