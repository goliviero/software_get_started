==============
Latex tutorial
==============

:Authors: Guillaume Oliviéro
:Date:    2023-02-22
:Contact: oliviero@lp2ib.in2p3.fr

.. contents::

.. figure:: img/logo_latex.png
   :width: 800

Goals of the tutorial
=====================

- Learn the LaTeX basics
- Provide some useful and basic skeletons covering most of usage


Introduction
============

What is LaTeX?
--------------

LaTeX  is  a document  preparation  system  widely used  in  academia,
particularly in STEM fields. As a PhD student, learning LaTeX can help
you produce high-quality documents, including research papers, theses,
and dissertations.  LaTeX allows you to  focus on the content  of your
document  while  the  system  takes care  of  formatting  and  layout.

Getting Started with LaTeX
--------------------------

To  get  started  with  LaTeX,  you  will  need  to  install  a  LaTeX
distribution on  your computer.  Some popular options  include MiKTeX,
TeX  Live,  and   MacTeX,  which  are  available   for  free  download
online. You  will also need a  LaTeX editor, which is  a software tool
that  allows you  to  write  and edit  LaTeX  documents. Some  popular
options include Overleaf, Texmaker, and Emacs.

Once you have installed a LaTeX distribution and editor, you can start
learning  how to  use LaTeX  by going  through tutorials  and examples
provided     online.     The      LaTeX     project     website     at
https://www.latex-project.org/ provides  documentation, tutorials, and
examples to help you get started with LaTeX.


Start here tutorial
===================

You must follow this nice  Overlea online tutorial where everything is
well explained:

https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes

What is Overleaf?
-----------------

Overleaf is a  web-based collaborative LaTeX editor  that allows users
to create, edit, and share LaTeX documents online. LaTeX is a document
preparation system that is widely  used in the academic and scientific
community to  create high-quality  documents such as  research papers,
technical reports, and theses.

Overleaf provides a user-friendly interface that allows multiple users
to work  on the same  document simultaneously, with  real-time updates
and collaboration tools such as chat  and commenting. This makes it an
ideal  tool for  teams working  on  joint projects,  such as  research
papers, dissertations, and conference presentations.

Overleaf also  provides a wide  range of  templates and tools  to help
users get started with LaTeX,  including document classes, styles, and
fonts. It  also offers an integrated  file manager, so you  can easily
manage and organize your LaTeX documents.

One of  the biggest advantages of  Overleaf is that it  eliminates the
need   for  users   to  install   and  manage   LaTeX  on   their  own
computers. Everything is done through  the web interface, so users can
access their documents from any device with an internet connection.


Some compilation examples
-------------------------

You     can    work     online    directly     on    the     `Overleaf
<https://www.overleaf.com/>`_ interface.

Or,  you can  generate  a  pdf document  from  a  latex (.tex)  source
file. Several applications can do it:

.. code:: sh

   $ pdflatex cv_en.tex

   # or

   $ latexmk -pdf cv_en.tex
..

Clean up temporary TEX files created for a specific TEX file:

.. code:: sh

   $ latexmk -c
..

Skeletons list
==============

- `PhD thesis skeleton <thesis_skeleton>`_
- `Article skeleton <article_skeleton>`_
- Book skeleton (TBD)
- `Beamer presentation skeleton <presentation_skeleton>`_
- `Curiculum skeleton and cover letter <cv_skeleton>`_




Differences between the ``book``, ``report``, and ``article`` classes
---------------------------------------------------------------------

Differences with regard to available commands and environments:

- ``book`` and ``report`` feature the ``\chapter`` sectioning command,
  while ``article`` doesn't.

- In ``book``  and ``report``, ``\appendix`` will  cause ``\chapters``
  to  be typeset  as ``Appendix  X``  instead of  ``Chapter X``.   For
  ``article``, this isn't applicable.

- ``book`` and ``report`` will start a new page for ``\parts`` , while
  ``article`` won't.

- ``book``   offers   the   ``\frontmatter``,   ``\mainmatter``,   and
  ``\backmatter`` commands  to control  page numbering (Roman  for the
  front matter,  arabic elsewhere) and numbering  of sectioning titles
  (no numbering  in the front  and back matter), while  ``report`` and
  ``article`` don't.

- ``book`` doesn't  offer the  abstract environment,  while ``report``
  and ``article`` do.

Differences with regard to default settings:

- The  ``book``  class uses  the  twoside  class option  (which  means
  different margins and headers/footers for even and odd pages), while
  ``report`` and ``article`` use oneside.

- ``book`` uses  openright (new  parts and  chapters start  on "right"
  pages, adding  a blank page  before if necessary),  while ``report``
  uses openany. (Note that "right" means  an odd page in twoside mode,
  but any  page in  oneside mode.)   For ``article``,  the distinction
  between openright and openany isn't applicable.

- ``book`` uses the headings pagestyle for non-chapter-starting pages,
  while ``report`` and ``article`` always use plain.

- ``book``  and  ``report`` use  titlepage  (the  title page  and  *if
  applicable* the  abstract environment  will be  typeset on  pages of
  their own), while ``article`` uses notitlepage.

- For  ``book`` and  ``report``, the  lowest-level sectioning  command
  which is  numbered and  incorporated into the  table of  contents is
  ``\subsection``, while for ``article`` it is ``\subsubsection``.

- ``book`` and ``report`` will use  the arguments of ``\chapters`` and
  ``\sections`` for  running headings (if such  headings are present),
  while ``article`` will use ``\sections`` and ``\subsections``.

- ``book`` and  ``report`` will number floats  (figures, tables etc.),
  equations, and footnotes per  chapter, while ``article`` will number
  them  continuously.  Note  that  footnotes, even  when numbered  per
  chapter, do not feature a chapter prefix.

- ``book``  and ``report``  will use  ``\bibname`` (which  defaults to
  ``Bibliography``) for the heading of bibliographic references, while
  ``article``    will   use    ``\refname``    (which   defaults    to
  ``References``).


Resources
=========

A gallery of LaTeX templates: https://www.overleaf.com/gallery
An other website for LaTeX templates: https://www.latextemplates.com/cat/articles
