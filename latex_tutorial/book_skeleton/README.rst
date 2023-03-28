=============
Book skeleton
=============

:Authors: Guillaume Oliviéro
:Date:    2023-03-22
:Contact: oliviero@lp2ib.in2p3.fr

.. contents::


Introduction
============

A LaTeX book skeleton  in english really close to what  we have in the
`thesis skeleton <../thesis_skeleton>`_. You can  use it as a base for
you PhD thesis and adapt it as you want.


Contents
========

The `main  document <main.tex>`_  is ``main.tex``.  It  contains basic
template for  a book. It contains  the different chapters of  the book
which are splitted into different tex file for an easier usage:

- `Introduction <others/introduction.tex>`_
- `Chapter 1 <chapter_1/chap_1.tex>`_
- `Chapter 2 <chapter_2/chap_2.tex>`_
- `Chapter 3 <chapter_3/chap_3.tex>`_
- `Conclusion <others/conclusion.tex>`_
- `Annexes <others/annexes.tex>`_
- `Abstract <others/abstract.tex>`_

And  a  `bibliography <bibliography.bib>`_  file  ``bibliography.bib``
where you can put all your references.

There  is an  other file  called ``packages.tex``  which contains  all
packages used to generate this tex document.


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
