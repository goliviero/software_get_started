==========================
Pandoc
==========================

:Authors: Guillaume Oliviéro
:Date:    2023-02-14
:Contact: oliviero@cenbg.in2p3.fr

.. contents::
   :depth: 2
..


Goal
====

Pandoc  is a  universal document  converter.  If  you need  to convert
files from one  markup format into another, pandoc  is your swiss-army
knife.   Pandoc can  convert between  a lot  of text  format including
Markdown, reStructuredText, HTML, LaTeX, Wiki format and of course PDF
format.

Some use cases
==============

``man pandoc`` for the list of options.

``-s`` option  means that the output  will be a standalone  file so it
generates proper header and footer.

``-t`` specify output format.

Markdown to PDF:
----------------

.. code:: sh

   $ pandoc  example.md -o example.pdf
..

Markdown to rst:
----------------

.. code:: sh

   $ pandoc -t rst -s example.md -o example.rst
..

LaTeX to Markdown:
------------------

.. code:: sh

   $ pandoc -s example4.tex -o example4.md
..

Markdown to HTML:
-----------------

.. code:: sh

   $ pandoc MANUAL.md -o MANUAL.html
..

Markdown to ipynb (Jupyter notebook):
-------------------------------------

.. code:: sh

   $ pandoc example.md -o example.ipynb
..

And many more examples you can find online.

Resources
=========

- Official website: https://pandoc.org/index.html
- Pandoc Manual: https://pandoc.org/MANUAL.html
- Demos page: https://pandoc.org/demos.html
