==============
Latex tutorial
==============

:Authors: Guillaume Oliviéro
:Date:    2023-02-22
:Contact: oliviero@cenbg.in2p3.fr

.. contents::

.. figure:: img/LaTeX_logo.svg
   :width: 1000

Goals of the tutorial
=====================

-

-

- Provide some useful skeletons covering most of usage


Introduction
============

Generate a pdf document from a latex source file. Several applications
can do it:

.. code:: sh

   $ pdflatex cv_en.tex

   # or

   $ latexmk -pdf cv_en.tex
..

Clean up temporary TEX files created for a specific TEX file:

.. code:: sh

   $ latexmk -c
..

Start here tutorial
===================

TBD

Skeletons list
==============

- Article skeleton (TBD)
- Book skeleton (TBD)
- `PhD thesis skeleton <thesis_skeleton>`_
- `Curiculum skeleton <cv_skeleton>`_
- `Beamer presentation skeleton <presentation_skeleton>`_




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
