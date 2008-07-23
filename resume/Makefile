origfile=hatem_nassrat
build=build
TEXF=$(build)/helvetica.sty  $(build)/res.cls
OBJS=$(build)/$(origfile).tex $(TEXF)
MIN=Makefile.in
MOUT=$(build)/Makefile


dvi : $(origfile).dvi

$(origfile).dvi: $(OBJS) $(MOUT)
	cd $(build); make -w dvi
	cp $(build)/$@ ./

pdf : $(origfile).pdf

$(origfile).pdf: $(OBJS) $(MOUT)
	cd $(build); make -w pdf
	cp $(build)/$@ ./

ps : $(origfile).ps

$(origfile).ps: $(OBJS) $(MOUT)
	cd $(build); make -w ps
	cp $(build)/$@ ./

tarball: $(origfile).tar.gz

$(origfile).tar.gz: clean $(TEXF) $(OBJS) $(MOUT)
	cd $(build); make -w tarball
	cp $(build)/$@ ./

html: $(origfile).html

$(origfile).html: $(HOBJS) $(OBJS) $(MOUT)
	cd $(build); make -w html
	cp $(build)/$@ ./

$(build)/%: %
	mkdir -p $(build)
	cp -r $< $@

$(MOUT): $(MIN)
	mkdir -p $(build)
	cp $(MIN) $(MOUT)
# 	cp $< $@

clean:
	rm -fr $(build)

spotless: clean
	rm -fr $(origfile).pdf $(origfile).ps $(origfile).dvi \
	$(origfile).tar.gz
