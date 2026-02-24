LATEXMK = latexmk
PDFDIR  = pdf

SUITE_SRC      = paper/main.tex
CORE_SRC       = paper/charter-core.tex
STANDARD_SRC   = paper/charter-technical-standard.tex
COMMENTARY_SRC = paper/charter-commentary.tex
SUITE_MAP_SRC  = paper/charter-suite-map.tex

SUITE_JOBNAME      = the-open-charter
CORE_JOBNAME       = the-open-charter-core
STANDARD_JOBNAME   = the-open-charter-technical-standard
COMMENTARY_JOBNAME = the-open-charter-commentary
SUITE_MAP_JOBNAME  = the-open-charter-suite-map

# Keep dependency tracking broad: split docs share a common preamble and
# section-part inputs under `paper/parts/`.
DEPS = $(wildcard paper/*.tex paper/parts/*.tex) paper/refs.bib

.PHONY: all zenodo clean veryclean
SOURCES_DUMP = paper/papers_combined.txt

.PHONY: sources

all: \
	$(PDFDIR)/$(SUITE_JOBNAME).pdf \
	$(PDFDIR)/$(CORE_JOBNAME).pdf \
	$(PDFDIR)/$(STANDARD_JOBNAME).pdf \
	$(PDFDIR)/$(COMMENTARY_JOBNAME).pdf \
	$(PDFDIR)/$(SUITE_MAP_JOBNAME).pdf

zenodo: \
	$(PDFDIR)/$(CORE_JOBNAME).pdf \
	$(PDFDIR)/$(STANDARD_JOBNAME).pdf \
	$(PDFDIR)/$(COMMENTARY_JOBNAME).pdf \
	$(PDFDIR)/$(SUITE_MAP_JOBNAME).pdf

sources: $(SOURCES_DUMP)

$(SOURCES_DUMP): scripts/generate_papers_combined.py $(DEPS)
	python3 scripts/generate_papers_combined.py

$(PDFDIR):
	mkdir -p $@

$(PDFDIR)/$(SUITE_JOBNAME).pdf: $(SUITE_SRC) $(DEPS) | $(PDFDIR)
	cd paper && TEXINPUTS="..:.:$(TEXINPUTS)" \
	  LC_ALL=C LANG=C $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error \
	  -jobname=$(SUITE_JOBNAME) -output-directory=../$(PDFDIR) main.tex

$(PDFDIR)/$(CORE_JOBNAME).pdf: $(CORE_SRC) $(DEPS) | $(PDFDIR)
	cd paper && TEXINPUTS="..:.:$(TEXINPUTS)" \
	  LC_ALL=C LANG=C $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error \
	  -jobname=$(CORE_JOBNAME) -output-directory=../$(PDFDIR) charter-core.tex

$(PDFDIR)/$(STANDARD_JOBNAME).pdf: $(STANDARD_SRC) $(DEPS) | $(PDFDIR)
	cd paper && TEXINPUTS="..:.:$(TEXINPUTS)" \
	  LC_ALL=C LANG=C $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error \
	  -jobname=$(STANDARD_JOBNAME) -output-directory=../$(PDFDIR) charter-technical-standard.tex

$(PDFDIR)/$(COMMENTARY_JOBNAME).pdf: $(COMMENTARY_SRC) $(DEPS) | $(PDFDIR)
	cd paper && TEXINPUTS="..:.:$(TEXINPUTS)" \
	  LC_ALL=C LANG=C $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error \
	  -jobname=$(COMMENTARY_JOBNAME) -output-directory=../$(PDFDIR) charter-commentary.tex

$(PDFDIR)/$(SUITE_MAP_JOBNAME).pdf: $(SUITE_MAP_SRC) $(DEPS) | $(PDFDIR)
	cd paper && TEXINPUTS="..:.:$(TEXINPUTS)" \
	  LC_ALL=C LANG=C $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error \
	  -jobname=$(SUITE_MAP_JOBNAME) -output-directory=../$(PDFDIR) charter-suite-map.tex

clean:
	cd paper && LC_ALL=C LANG=C $(LATEXMK) -C -jobname=$(SUITE_JOBNAME) -output-directory=../$(PDFDIR) main.tex
	cd paper && LC_ALL=C LANG=C $(LATEXMK) -C -jobname=$(CORE_JOBNAME) -output-directory=../$(PDFDIR) charter-core.tex
	cd paper && LC_ALL=C LANG=C $(LATEXMK) -C -jobname=$(STANDARD_JOBNAME) -output-directory=../$(PDFDIR) charter-technical-standard.tex
	cd paper && LC_ALL=C LANG=C $(LATEXMK) -C -jobname=$(COMMENTARY_JOBNAME) -output-directory=../$(PDFDIR) charter-commentary.tex
	cd paper && LC_ALL=C LANG=C $(LATEXMK) -C -jobname=$(SUITE_MAP_JOBNAME) -output-directory=../$(PDFDIR) charter-suite-map.tex
	rm -f $(PDFDIR)/$(SUITE_JOBNAME).*
	rm -f $(PDFDIR)/$(CORE_JOBNAME).*
	rm -f $(PDFDIR)/$(STANDARD_JOBNAME).*
	rm -f $(PDFDIR)/$(COMMENTARY_JOBNAME).*
	rm -f $(PDFDIR)/$(SUITE_MAP_JOBNAME).*
	# Clean up common editor/IDE artifacts when builds are run outside the Makefile.
	rm -f main.aux main.bbl main.blg main.fdb_latexmk main.fls main.log main.out main.pdf main.synctex.gz main.toc
	rm -f charter-core.aux charter-core.bbl charter-core.blg charter-core.fdb_latexmk charter-core.fls charter-core.log charter-core.out charter-core.pdf charter-core.synctex.gz charter-core.toc
	rm -f charter-technical-standard.aux charter-technical-standard.bbl charter-technical-standard.blg charter-technical-standard.fdb_latexmk charter-technical-standard.fls charter-technical-standard.log charter-technical-standard.out charter-technical-standard.pdf charter-technical-standard.synctex.gz charter-technical-standard.toc
	rm -f charter-commentary.aux charter-commentary.bbl charter-commentary.blg charter-commentary.fdb_latexmk charter-commentary.fls charter-commentary.log charter-commentary.out charter-commentary.pdf charter-commentary.synctex.gz charter-commentary.toc
	rm -f paper/main.aux paper/main.bbl paper/main.blg paper/main.fdb_latexmk paper/main.fls paper/main.log paper/main.out paper/main.pdf paper/main.synctex.gz paper/main.toc
	rm -f paper/charter-core.aux paper/charter-core.bbl paper/charter-core.blg paper/charter-core.fdb_latexmk paper/charter-core.fls paper/charter-core.log paper/charter-core.out paper/charter-core.pdf paper/charter-core.synctex.gz paper/charter-core.toc
	rm -f paper/charter-technical-standard.aux paper/charter-technical-standard.bbl paper/charter-technical-standard.blg paper/charter-technical-standard.fdb_latexmk paper/charter-technical-standard.fls paper/charter-technical-standard.log paper/charter-technical-standard.out paper/charter-technical-standard.pdf paper/charter-technical-standard.synctex.gz paper/charter-technical-standard.toc
	rm -f paper/charter-commentary.aux paper/charter-commentary.bbl paper/charter-commentary.blg paper/charter-commentary.fdb_latexmk paper/charter-commentary.fls paper/charter-commentary.log paper/charter-commentary.out paper/charter-commentary.pdf paper/charter-commentary.synctex.gz paper/charter-commentary.toc
	rm -f paper/charter-suite-map.aux paper/charter-suite-map.bbl paper/charter-suite-map.blg paper/charter-suite-map.fdb_latexmk paper/charter-suite-map.fls paper/charter-suite-map.log paper/charter-suite-map.out paper/charter-suite-map.pdf paper/charter-suite-map.synctex.gz paper/charter-suite-map.toc

veryclean: clean
	rm -f $(PDFDIR)/$(SUITE_JOBNAME).pdf
	rm -f $(PDFDIR)/$(CORE_JOBNAME).pdf
	rm -f $(PDFDIR)/$(STANDARD_JOBNAME).pdf
	rm -f $(PDFDIR)/$(COMMENTARY_JOBNAME).pdf
	rm -f $(PDFDIR)/$(SUITE_MAP_JOBNAME).pdf
