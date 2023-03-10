================
Article skeleton
================

:Authors: Guillaume Oliviéro
:Date:    2023-03-10
:Contact: oliviero@cenbg.in2p3.fr

.. contents::


Contents
========

The `main document <main_article.tex>`_ is ``main_article.tex``.  It contains basic template
for a two  columns article. It contains the different  sections of the
article  which are  splitted into  different  tex file  for an  easier
usage:

- `Introduction <sections/introduction.tex>`_
- `Section      1      <sections/section_1.tex>`_,     `Section      2
  <sections/section_2.tex>`_, `Section 3 <sections/section_3.tex>`_
- `Conclusion <sections/conclusion.tex>`_
- `Acknowledgments <sections/acknowledgments.tex>`_

And  a  `bibliography <bibliography.bib>`_  file  ``bibliography.bib``
where you can put all your references.


Usage
=====

A `Makefile <GNUmakefile>`_ called ``GNUmakefile`` is here to help you
compiling the latex document. To build  and compile the latex file, in
your terminal, you just have to type:

.. code:: sh

   $ make
..

To  remove and  clean your  repository  from all  non-source tex  file
except the output PDF file, just type:

.. code:: sh

   $ make clean
..
