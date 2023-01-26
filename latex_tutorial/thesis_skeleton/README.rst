==========================================
Git rédaction de thèse (version francaise)
==========================================

:Authors : G.Oliviéro <goliviero@lpccaen.in2p3.fr>

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

=====================================
Git for PhD writing (english version)
=====================================

:Authors : G.Oliviéro <goliviero@lpccaen.in2p3.fr>
