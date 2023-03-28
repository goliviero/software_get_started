MAIN=main
SOURCES := $(shell find . -name '*.tex')

.PHONY : all pdf view clean
all : pdf

SUFFIXES : .tex .fig .pdf .pdftex .pdftex_t .pdf


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
	$(RM) chapter_*/*.aux
	$(RM) others/*.aux
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

.PHONY : all pdf view clean
pdf : $(MAIN).pdf

$(MAIN).pdf : $(MAIN).tex $(SOURCES)
	pdflatex $<
	bibtex $(MAIN)
	pdflatex $<
	pdflatex $<
