
MAIN=main_article

.PHONY : all
all : pdf

SUFFIXES : .tex .fig .pdftex .pdftex_t .pdf


.PHONY : clean
clean :
	find . -name "*~" -exec $(RM) \{\} \;
	find . -name "*.fig.bak" -exec $(RM) \{\} \;
	find . -name "*.aux" -exec $(RM) \{\} \;
	find . -name "*.bbl" -exec $(RM) \{\} \;
	find . -name "*.blg" -exec $(RM) \{\} \;
	$(RM) $(MAIN).log
	$(RM) $(MAIN).nav
	$(RM) $(MAIN).out
	$(RM) $(MAIN).snm
	$(RM) $(MAIN).toc
	$(RM) $(MAIN).bbl
	$(RM) $(MAIN).blg
	$(RM) $(MAIN).brf
	$(RM) *.blg
	$(RM) *.snm
	$(RM) *.toc
	$(RM) *.bbl
	$(RM) *.blg
	$(RM) *.aux
	$(RM) *.acn
	$(RM) *.glo
	$(RM) *.tdo
	$(RM) *.lof
	$(RM) *.lot
	$(RM) *.mtc*
	$(RM) *.ntn
	$(RM) *.xdy
	$(RM) *.maf
	$(RM) missfont.log

.PHONY : pdf
pdf : $(MAIN).pdf

$(MAIN).pdf : $(MAIN).tex
	pdflatex $<
	bibtex $(MAIN)
	pdflatex $<
	pdflatex $<
