PDFLATEX=pdflatex
src = $(wildcard *.tex)
obj = $(src:.tex=.pdf)

all: revised.pdf errata.pdf

%.pdf: %.tex
	latexmk \
	-pdf \
	-silent \
	-use-make $<

core: $(obj)

.PHONY: clean
clean:
	rm -f $(obj) $(obj:.pdf=.aux) $(obj:.pdf=.out) $(obj:.pdf=.aux) $(obj:.pdf=.log) $(obj:.pdf=.toc) paths.aux $(obj:.pdf=.fls) $(obj:.pdf=.fdb_latexmk)
