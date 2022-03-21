Title: Identifying branded keywords in Excel
Date: 2022-03-20 15:59
Category: SEO
Tags: Excel
Author: Freddie Larkins
Summary: It’s always helpful to identify branded terms when you’re dealing with a list of keywords. Filtering them out gives you a view on non-branded performance and potential areas of improvement.
Slug: identifying-branded-keywords-in-excel

**Any large-scale analysis of a group of keywords is always enhanced by identifying branded and non-branded keywords. Thankfully, it's simple to do in Excel.**

## The formula
Assuming your keywords are in column A, this formula should do the trick:

```
=IF(ISNUMBER(SEARCH("BRANDNAME",A2)),"Branded","Non-branded")
```

Just replace `BRANDNAME` with the brand that you’re working, copy and paste the formula into Excel and apply it to the entire column of keywords. That’ll give you a column with either a 'Branded' or 'Non-branded' value for each keyword.

## How it works
Let’s break down each part of the formula, working inside out. We’ll use an example set of Nike keywords to illustrate each step.

### The SEARCH function

The [SEARCH function](https://exceljet.net/excel-functions/excel-search-function) looks for the provided string of text inside another [string](https://www.deskbright.com/excel/excel-string-functions/) of text, returning the position of the first character in the case of a match. It’s not case sensitive. In our case, `=SEARCH("nike",A2)` is asking Excel to look for the text “nike” inside our keyword text string.

![Screenshot of an Excel table demonstrating the application of the SEARCH function to a set of keywords.](/images/search-function-screenshot.png)

If it is present, the formula will return the position of the “n” in “nike”. If it is not present, the formula will evaluate as a #VALUE! error.

### The ISNUMBER function

The [ISNUMBER function](https://exceljet.net/excel-functions/excel-isnumber-function) simply checks that a given cell is a number, returning either TRUE or FALSE. Thus, our formula becomes `=ISNUMBER(SEARCH("nike"),A2)`:

![Screenshot of an Excel table demonstrating the application of the SEARCH function in conjunction with ISNUMBER to a set of keywords.](/images/search-and-isnumber-functions.png)

By wrapping our `SEARCH` function with `ISNUMBER`, we’re converting the output of the former into a Boolean TRUE or FALSE value. In other words:

*   If “nike” is _present_ in keyword –> `SEARCH` returns a number –> `ISNUMBER` evaluates as TRUE
*   If “nike” is _not present_ in keyword –> `SEARCH` returns an #VALUE! error –> `ISNUMBER` evaluates as FALSE

Essentially, we’re converting the results of `SEARCH` into something we can use in the final component of the formula, our `IF` statement.

### The IF function

The [IF function](https://exceljet.net/excel-functions/excel-if-function) uses a logical test to return one value for a TRUE result, and another for FALSE.

We bring everything together using an `IF` statement: `=IF(ISNUMBER(SEARCH("BRANDNAME",A2)),"Branded","Non-branded")`

![Screenshot of an Excel table showing the full function](/images/search-isnumber-and-if-functions.png)

Our logical test is the `ISNUMBER(...)` component of the function. If that evaluates as TRUE, the `IF` statement returns “Branded”. If FALSE, it returns “Non-branded”.

**And that’s it!**

I use this function without fail when I’m dealing with lists of keywords. After reading this, hopefully you will too.