all: slides.pdf

%.pdf: %.tex
	@pdflatex $^ && pdflatex $^

clean:
	@rm -vf *.log *.out *.aux *~ *.tns *.nav *.snm *.toc

clean+: clean
	@rm -vf *.pdf
