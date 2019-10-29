PDFLATEX=pdflatex
src = $(wildcard *.tex)
obj = $(src:.tex=.pdf)

%.pdf: %.tex
	$(PDFLATEX) $<

core: $(obj)

.PHONY: clean
clean:
	rm -f $(obj)
