================================
PhD skeleton (version francaise)
================================

:Authors: Guillaume Oliviéro
:Date:    2023-02-22
:Contact: oliviero@lp2ib.in2p3.fr

.. contents::

Structure du répertoire LaTeX
=============================

Structure du Main
-----------------

Main.tex : fichier principal latex incluant
 * Le préambule (package + options) Preambule.tex
 * Les commandes et environnements persos CommandesPerso.tex
 * La page de garde img/page_de_garde.pdf
 * La liste des figures
 * La liste des tableaux
 * Tous les chapitres situés dans les dossiers Chapitre_X/chap_X.tex
 * Les annexes Annexes.tex


Structure des repository des chapitres
--------------------------------------

* chap_X.tex : fichier latex pour le chapitre correspondant
* Chapitre_X/fig : dossier sources XFIG (logiciel permettant de faire facilement des schémas)
* Chapitre_X/img : dossier sources des images png / pdf


Compilation
===========

* make : compile le document avec tous les chapitres
* make clean : nettoie tous les produits de compilation / build



Git for PhD writing (english version)
=====================================

Have to translate all directories and files...

But in fact, the latex book skeleton  template is very close to what a
PhD thesis is so you can  check `this page <../book_skeleton>`_ on the
repository  to  have a  ``book``  skeleton  example  that can  be  the
starting point fort a PhD thesis in english.
