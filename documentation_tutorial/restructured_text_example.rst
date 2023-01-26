==========================
Restructured text tutorial
==========================

:Authors: Guillaume Oliviéro
:Date:    2023-01-26
:Contact: oliviero@cenbg.in2p3.fr

.. contents::
   :depth: 3
..

.. _BxCppDev: https://github.com/TYYYYY

.. raw:: pdf

   PageBreak oneColumn

=====

Section
-------

Subsection


If you  want to use  the development version (possibly  unstable), please use
Git:

.. code:: sh

   $ cd ${HOME}
   $ mkdir -p ${HOME}/BxCppDev
   $ cd ${HOME}/BxCppDev
   $ git clone https://github.com/BxCppDev/Bayeux Bayeux.git
   $ cd Bayeux.git
   $ git checkout develop
..

.. raw:: pdf


Core Software Required
......................

* CMake 3.10.2 or higher: http://www.cmake.org

  * Ubuntu 18.04 provides CMake version 3.10.2.
  * Ubuntu 20.04 provides CMake version 3.16.3.

* C/C++ compiler supporting at least C++11 standard
  (GNU/Clang/Intel)

  * Ubuntu 18.04 provides GCC version 6.5 and 7.3.
  * Ubuntu 20.04 provides GCC version 9.3.
  * Bayeux is known to work on CentOS with GCC 4.9

On Linux,  you should  install these through  the package  manager for
your distribution. Some older  Linux systems (SL/CentOS, especially on
institutional computing clusters)  may not provide CMake  3.3. If this
is the  case, then you should  download the latest Linux  *binary .sh*
file (example: ``cmake-3.17.2-Linux-x86_64.sh``) from:



Bayeux Configuration Options
----------------------------

These options control the core configuration of Bayeux.

``BAYEUX_CXX_STANDARD``
  Select the C++  Standard to compile against. Recognized values are:

     * ``11`` (default) : all features of the C++11 standard in GCC 4.9 (provided
       for forward compatibility)
     * ``14``  :  same  as  ``11``  plus at  least  one  C++14  feature
       (provided for forward compatibility)
     * ``17``  :  same  as  ``14``  plus at  least  one  C++17  feature
       (provided for forward compatibility)
     * ``20``  :  same  as  ``17``  plus at  least  one  C++20  feature
       (provided for forward compatibility)

``BAYEUX_COMPILER_ERROR_ON_WARNING``
  Turn warnings into errors. Default is ON.
