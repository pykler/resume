resume=hatem_nassrat
cover=$(resume)_cover_letter
build=build
TEXF=helvetica.sty  res.cls
HUTIL=tth2html.py
OBJS=${addprefix $(build)/, $(resume).tex $(TEXF) $(cover).tex}
MIN=Makefile.in
MOUT=$(build)/Makefile

usage:
	@echo The following targets are acceptable
	@echo
	@echo apdf advi aps ahtml tarball dvi pdf ps html cdvi cpdf cps chtml
	@echo
	@echo All the targets starting with \"a\" create both resume and cover
	@echo letter while the ones without a prefix only create the resume
	@echo and the remainder only create the cover letter.
	@echo 
	@echo tarball creates a tarball of both tex files and dependencies
	@echo 

.PHONY: apdf advi aps ahtml tarball dvi pdf ps html cdvi cpdf cps chtml

apdf: pdf cpdf
advi: dvi cdvi
aps: ps cps
ahtml: html chtml
tarball: $(resume).tar.gz

dvi : $(resume).dvi
pdf : $(resume).pdf
ps : $(resume).ps
html: $(resume).html

cdvi : $(cover).dvi
cpdf : $(cover).pdf
cps : $(cover).ps
chtml: $(cover).html

%.dvi: $(OBJS) $(MOUT)
	cd $(build); make -w $@ 
	cp $(build)/$@ ./

%.pdf: $(OBJS) $(MOUT)
	cd $(build); make -w $@
	cp $(build)/$@ ./

%.ps: $(OBJS) $(MOUT)
	cd $(build); make -w $@
	cp $(build)/$@ ./

%.html: $(HOBJS) $(OBJS) $(MOUT) $(HUTIL)
	cd $(build); make -w $@
	cp $(build)/$@ ./

%.tar.gz: clean $(TEXF) $(OBJS) $(MOUT)
	cd $(build); make -w $@
	cp $(build)/$@ ./

$(build)/%: %
	mkdir -p $(build)
	cp -r $< $@

$(MOUT): $(MIN)
	mkdir -p $(build)
	cp $(MIN) $(MOUT)

clean:
	rm -fr $(build)

distclean: clean
	rm -fr $(resume).pdf $(resume).ps $(resume).dvi $(resume).tar.gz
	rm -fr $(cover).pdf $(cover).ps $(cover).dvi $(cover).tar.gz

# vim: set noet:
