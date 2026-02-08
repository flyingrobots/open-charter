LATEXMK = latexmk
SRC     = paper/main.tex
DEPS    = paper/charter_body.tex paper/charter_meta.tex paper/refs.bib
JOBNAME = the-open-charter
PDFDIR  = pdf

.PHONY: all clean veryclean

all: $(PDFDIR)/$(JOBNAME).pdf

$(PDFDIR):
	mkdir -p $@

$(PDFDIR)/$(JOBNAME).pdf: $(SRC) $(DEPS) | $(PDFDIR)
	cd paper && TEXINPUTS="..:.:$(TEXINPUTS)" \
	  LC_ALL=C LANG=C $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error \
	  -jobname=$(JOBNAME) -output-directory=../$(PDFDIR) main.tex

clean:
	cd paper && LC_ALL=C LANG=C $(LATEXMK) -C -jobname=$(JOBNAME) -output-directory=../$(PDFDIR) main.tex
	rm -f $(PDFDIR)/$(JOBNAME).*
	# Clean up common editor/IDE artifacts when builds are run outside the Makefile.
	rm -f main.aux main.bbl main.blg main.fdb_latexmk main.fls main.log main.out main.pdf main.synctex.gz main.toc
	rm -f paper/main.aux paper/main.bbl paper/main.blg paper/main.fdb_latexmk paper/main.fls paper/main.log paper/main.out paper/main.pdf paper/main.synctex.gz paper/main.toc

veryclean: clean
	rm -f $(PDFDIR)/$(JOBNAME).pdf
