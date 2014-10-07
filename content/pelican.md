Title: Pelican post
Date: 2013-10-06 18:13
Category: Test

![alternate text](https://unsplash.imgix.net/uploads%2F14114036359651bd991f1%2Fb3ed8fdf?q=75&fm=jpg&auto=format&s=48ce2bc496d68ba261521169af4f0624)

Most URLs will automatically be turned into links. To be explicit, just write it like this:
<http://someurl>
<somebbob@example.com>

To use text for the link, write it:
[like this](http://someurl)

You can add a *title* (which shows up under the cursor):
[like this](http://someurl "this title shows up when you hover")

You can also put the [link URL][1] below the current paragraph
like [this][2].

   [1]: http://url
   [2]: http://another.url "A funky title"

Or you can use a [shortcut][] reference, which links the text "shortcut" to the link named "[shortcut]" on the next paragraph.
Or you can use a [shortcut][] reference, which links the text
"shortcut" to the link named "[shortcut]" on the next paragraph.

[shortcut]: http://goes/with/the/link/name/text

Use * or _ to emphasize things:
*this is in italic*  and _so is this_
**this is in bold**  and __so is this__
***this is bold and italic***  and ___so is this___

You can strike through text using HTML like this:
<s>this is strike through text</s>

A carriage return
makes a line break.

Two carriage returns make a new paragraph.

Use the > character in front of a line, just like in email
> Use it if you're quoting a person, a song or whatever.

> You can use *italic* or lists inside them also.
And just like with other paragraphs,
all of these lines are still
part of the blockquote, even without the > character in front.

To end the blockquote, just put a blank line before the following
paragraph.

If you want some text to show up exactly as you write it, without Markdown doing anything to it, just indent every line by at least 4 spaces (or 1 tab). As an alternative to indenting, you can use 4 or more tildes before and after the text.

 This line won't *have any markdown* formatting applied.
    I can even write <b>HTML</b> and it will show up as text.
    This is great for showing program source code, or HTML or even
    Markdown. <b>this won't show up as HTML</b> but
    exactly <i>as you see it in this text file</i>.

Within a paragraph, you can use backquotes to do the same thing.
`This won't be *italic* or **bold** at all.`

* an asterisk starts an unordered list
* and this is another item in the list
+ or you can also use the + character
- or the - character

To start an ordered list, write this:

1. this starts a list *with* numbers
+  this will show as number "2"
*  this will show as number "3."
9. any number, +, -, or * will keep the list going.
    * just indent by 4 spaces (or tab) to make a sub-list
        1. keep indenting for more sub lists
    * here i'm back to the second level

You can create tables using pipes and dashes like this:
  First Header  | Second Header
  ------------- | -------------
  Content Cell  | Content Cell
  Content Cell  | Content Cell

Just put 1 or more dashes or equals signs (--- or ===) below the title.
This is a huge header
==================

this is a smaller header
------------------

Just put three or more *'s or -'s on a line:
----------------

Or, you can use single spaces between then, like this:
* * *

or
- - - - - - -

To include an image, just put a "!" in front of a text link:
![alternate text](https://sourceforge.net/images/icon_linux.gif)

You can also use a title if you want, like this:
![tiny arrow](https://sourceforge.net/images/icon_linux.gif "tiny arrow")

To embed a YouTube video, use the `embed` macro (only YouTube is supported at this time):
[[embed url=http://www.youtube.com/watch?v=6YbBmqUnoQM]]

What if you want to just show asterisks, not italics?
* this shows up in italics: *a happy day*
* this shows the asterisks: \*a happy day\*

More ways of doing headers:
# this is a huge header #
## this is a smaller header ##
### this is even smaller ###
#### more small ####
##### even smaller #####
###### smallest still: `<h6>` header

[TOC]

# Section 1
## Sub-section 1
# Section 2

  :::python
    # Code goes here ...

You can also designate a code block by surrounding it with lines of tildes

~~~~~~
<a href="#">My code</a>
~~~~~~
