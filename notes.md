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


https://serverfault.com/questions/520195/how-does-servername-and-serveralias-work

https://www.digitalocean.com/community/tutorials/apache-configuration-error-ah00558-could-not-reliably-determine-the-server-s-fully-qualified-domain-name

https://devanswers.co/get-real-client-ip-address-cloudflare-apache-php/


https://stackoverflow.com/questions/20929606/what-are-the-numbers-after-the-http-status-codes-in-app-engines-dev-appserver-p


https://askubuntu.com/questions/476041/how-do-i-make-rsync-delete-files-that-have-been-deleted-from-the-source-folder