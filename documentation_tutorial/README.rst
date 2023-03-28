=================================
Documentation languages tutorials
=================================

:Authors: Guillaume Oliviéro
:Date:    2023-02-22
:Contact: oliviero@lp2ib.in2p3.fr

.. contents::

Goals of the tutorial
=====================

-
-
-


Introduction to documentation languages
=======================================

What is Restructured Text (or rst)?
-----------------------------------

Restructured Text (reST) is a lightweight markup language that is used
for   creating  structured   documents,  particularly   for  technical
documentation. reST is  easy to read and write, and  is designed to be
both human-readable  and machine-readable. As a  software teacher, you
may encounter  reST when  working on  documentation for  your software
projects.

reST  is  used by  many  popular  documentation tools  and  platforms,
including Sphinx, Read the Docs, and GitHub. With reST, you can create
professional-looking  documentation  that  is  easy  to  navigate  and
understand.

What is MarkDown (or md)?
-------------------------

MarkDown is  a lightweight markup  language that is used  for creating
formatted documents, particularly for web content. MarkDown is easy to
read  and  write,  and  is  designed to  be  both  human-readable  and
machine-readable. As  a software  teacher, you may  encounter MarkDown
when working on  documentation for your software  projects or creating
content for the  web. MarkDown is used by many  popular web platforms,
including GitHub, Stack Overflow, and Reddit.

Getting Started with reST or MarkDown
-------------------------------------

To get started with reST or MarkDown, all you need is a text editor and
a basic  understanding of  its syntax.   reST or  MarkDown files  use a
simple syntax  that is based  on plain text, so  you can use  any text
editor to create and edit reST files.

The basic elements of reST or MarkDown syntax include:

- Headings and  subheadings
- Lists, which can be unordered (bulleted) or ordered (numbered)
- Inline formatting, such as bold and italic text
- Code blocks, which are indicated by indentation
- Hyperlinks, which can be added using a simple syntax

Differences between reST and MarkDown
-------------------------------------

MarkDown and  Restructured Text are both  lightweight markup languages
that are commonly used  for creating formatted documents, particularly
for web content.  However, there  are some differences between the two
languages:

- Syntax: MarkDown uses a simpler  syntax than Restructured Text, with
  a smaller set of formatting elements.  This makes it easier to learn
  and use for  basic formatting needs, but can  limit its capabilities
  for more complex formatting.

- Features:  Restructured   Text  has  more  advanced   features  than
  MarkDown, such as support for table of contents, footnotes, and more
  sophisticated  image  handling.   MarkDown  is  generally  used  for
  simpler documents, while Restructured Text is better suited for more
  complex ones.

- Extensibility: Restructured  Text is more extensible  than MarkDown,
  with support for custom directives and roles. This makes it possible
  to extend the functionality of the language to meet specific needs.

- Toolchain:  Restructured Text  has a  more extensive  toolchain than
  arkdown, with  support for documentation generators  like Sphinx and
  advanced  publishing  workflows.   MarkDown  is  better  suited  for
  simpler workflows.

Overall, MarkDown  is a simpler language  that is easier to  learn and
use for basic formatting needs.  Restructured Text, on the other hand,
is  more advanced  and extensible,  making it  better suited  for more
complex documents and workflows.

Introduction to Pandoc
======================

What is Pandoc?
---------------

Pandoc is a command-line tool for converting documents from one format
to another.  It supports  a wide  range of  input and  output formats,
including Markdown, HTML,  LaTeX, PDF, and many others.  As a software
teacher, you may  find Pandoc useful for  converting documents between
formats  or  generating  documentation  for  your  software  projects.

Getting Started with Pandoc
---------------------------

To get started with Pandoc, you'll  need to download and install it on
your computer. Pandoc is available  for Windows, macOS, and Linux, and
can    be     downloaded    from     the    official     website    at
https://pandoc.org/. Once  you have installed  Pandoc, you can  use it
from the command line to convert documents between formats.

To  convert a  document  using  Pandoc, you  simply  run the  "pandoc"
command followed by the input file  and the desired output format. For
example,  to convert  a  Markdown  file to  HTML,  you  would run  the
following command:

.. code:: sh

   $ pandoc input.md -o output.html
..

Pandoc also supports a wide range of options and extensions, which can
be  used  to customize  the  output  and  behavior of  the  conversion
process. You can find more information on these options and extensions
in  the   Pandoc  documentation.   See  also   this  `pandoc  tutorial
<pandoc_tutorial.rst>`_ with some common examples.

Resources
=========

RST
---

https://docs.github.com/en/get-started/writing-on-github
Official RST website: https://docutils.sourceforge.io/rst.html
RST Quick reference: https://docutils.sourceforge.io/docs/user/rst/quickref.html
RST cheatsheet: https://docutils.sourceforge.io/docs/user/rst/cheatsheet.txt
Sphinx doc: https://sublime-and-sphinx-guide.readthedocs.io/en/latest/#work-with-rst-content

MarkDown
--------

Reference guides for Basic syntax: https://www.MarkDownguide.org/basic-syntax and Extended syntax: https://www.MarkDownguide.org/extended-syntax

https://fossil-scm.org/home/md_rules


Differences between MarkDown and RST
------------------------------------

https://gist.github.com/javiertejero/4585196
