===================================================
 The reStructuredText Cheat Sheet: Syntax Reminders
===================================================

:Authors: Guillaume Oliviéro
          David Goodger <goodger@python.org>
:Contact: oliviero@cenbg.in2p3.fr
:Date:    2023-02-03
:Info:    See <https://docutils.sourceforge.io/rst.html> for introductory docs.

.. contents::

Section Structure
=================

Section titles are underlined or overlined & underlined.

Body Elements
=============

Grid table:

+--------------------------------+-----------------------------------+
| Paragraphs are flush-left,     | Literal block, preceded by "::":: |
| separated by blank lines.      |                                   |
|                                |     Indented                      |
|     Block quotes are indented. |                                   |
+--------------------------------+ or::                              |
| >>> print 'Doctest block'      |                                   |
| Doctest block                  | > Quoted                          |
+--------------------------------+-----------------------------------+
| | Line blocks preserve line breaks & indents. [new in 0.3.6]       |
| |     Useful for addresses, verse, and adornment-free lists; long  |
|       lines can be wrapped with continuation lines.                |
+--------------------------------------------------------------------+

Simple tables:

================  ============================================================
List Type         Examples (syntax in the `text source <cheatsheet.txt>`_)
================  ============================================================
Bullet list       * items begin with "-", "+", or "*"
Enumerated list   1. items use any variation of "1.", "A)", and "(i)"
                  #. also auto-enumerated
Definition list   Term is flush-left : optional classifier
                      Definition is indented, no blank line between
Field list        :field name: field body
Option list       -o  at least 2 spaces between option & description
================  ============================================================

================  ============================================================
Explicit Markup   Examples (visible in the `text source`_)
================  ============================================================
Footnote          .. [1] Manually numbered or [#] auto-numbered
                     (even [#labelled]) or [*] auto-symbol
Citation          .. [CIT2002] A citation.
Hyperlink Target  .. _reStructuredText: https://docutils.sourceforge.io/rst.html
                  .. _indirect target: reStructuredText_
                  .. _internal target:
Anonymous Target  __ https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
Directive ("::")  .. image:: img/invaders_logo.png
                     :width: 500
Substitution Def  .. |substitution| replace:: like an inline directive
Comment           .. is anything else
Empty Comment     (".." on a line by itself, with blank lines before & after,
                  used to separate indentation contexts)
================  ============================================================

Inline Markup
=============

*emphasis*; **strong emphasis**; `interpreted text`; `interpreted text with role`:emphasis:; ``inline literal text``; standalone hyperlink, https://docutils.sourceforge.io; named reference, reStructuredText_; `anonymous reference`__; footnote reference, [1]_; citation reference, [CIT2002]_; |substitution|; _`inline internal target`.

Directive Quick Reference
=========================

See <https://docutils.sourceforge.io/docs/ref/rst/directives.html> for full info.

================  ============================================================
Directive Name    Description (Docutils version added to, in [brackets])
================  ============================================================
attention         Specific admonition; also "caution", "danger",
                  "error", "hint", "important", "note", "tip", "warning"
                  Example : .. note:: My note
admonition        Generic titled admonition: ``.. admonition:: By The Way``
image             ``.. image:: picture.png``; many options possible
figure            Like "image", but with optional caption and legend
topic             ``.. topic:: Title``; like a mini section
sidebar           ``.. sidebar:: Title``; like a mini parallel document
parsed-literal    A literal block with parsed inline markup
rubric            ``.. rubric:: Informal Heading``
epigraph          Block quote with class="epigraph"
highlights        Block quote with class="highlights"
pull-quote        Block quote with class="pull-quote"
compound          Compound paragraphs [0.3.6]
container         Generic block-level container element [0.3.10]
table             Create a titled table [0.3.1]
list-table        Create a table from a uniform two-level bullet list [0.3.8]
csv-table         Create a table from CSV data [0.3.4]
contents          Generate a table of contents
sectnum           Automatically number sections, subsections, etc.
header, footer    Create document decorations [0.3.8]
target-notes      Create an explicit footnote for each external target
math              Mathematical notation (input in LaTeX format)
meta              Document metadata
include           Read an external reST file as if it were inline
raw               Non-reST data passed untouched to the Writer
replace           Replacement text for substitution definitions
unicode           Unicode character code conversion for substitution defs
date              Generates today's date; for substitution defs
class             Set a "class" attribute on the next element
role              Create a custom interpreted text role [0.3.2]
default-role      Set the default interpreted text role [0.3.10]
title             Set the metadata document title [0.3.10]
================  ============================================================

Interpreted Text Role Quick Reference
=====================================

See <https://docutils.sourceforge.io/docs/ref/rst/roles.html> for full info.

================  ============================================================
Role Name         Description
================  ============================================================
emphasis          Equivalent to *emphasis*
literal           Equivalent to ``literal`` but processes backslash escapes
math              Mathematical notation (input in LaTeX format)
PEP               Reference to a numbered Python Enhancement Proposal
RFC               Reference to a numbered Internet Request For Comments
raw               For non-reST data; cannot be used directly (see docs) [0.3.6]
strong            Equivalent to **strong**
sub               Subscript
sup               Superscript
title             Title reference (book, etc.); standard default role
================  ============================================================

Resources
=========

An other good RST cheat sheet: https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst
