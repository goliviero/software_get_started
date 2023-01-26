# -*- mode: make; -*-

MAIN_DIR=.
MAIN_XFIG_DIR=$(MAIN_DIR)/fig
MAIN_PDFTEX_DIR=$(MAIN_DIR)/pdftex
MAIN_PDFTEX_T_DIR=$(MAIN_DIR)/pdftex_t

CHAP1_DIR=Chapitre_1
CHAP1_XFIG_DIR=$(CHAP1_DIR)/fig
CHAP1_PDFTEX_DIR=$(CHAP1_DIR)/pdftex
CHAP1_PDFTEX_T_DIR=$(CHAP1_DIR)/pdftex_t

$(info "DEBUG : CHAP1_DIR is " $(CHAP1_DIR))
$(info "DEBUG : CHAP1_XFIG_DIR is " $(CHAP1_XFIG_DIR))
$(info "DEBUG : CHAP1_PDFTEX_DIR is " $(CHAP1_PDFTEX_DIR))
$(info "DEBUG : CHAP1_PDFTEX_T_DIR is " $(CHAP1_PDFTEX_T_DIR))

CHAP2_DIR=Chapitre_2
CHAP2_XFIG_DIR=$(CHAP2_DIR)/fig
CHAP2_PDFTEX_DIR=$(CHAP2_DIR)/pdftex
CHAP2_PDFTEX_T_DIR=$(CHAP2_DIR)/pdftex_t

CHAP3_DIR=Chapitre_3
CHAP3_XFIG_DIR=$(CHAP3_DIR)/fig
CHAP3_PDFTEX_DIR=$(CHAP3_DIR)/pdftex
CHAP3_PDFTEX_T_DIR=$(CHAP3_DIR)/pdftex_t

CHAP4_DIR=Chapitre_4
CHAP4_XFIG_DIR=$(CHAP4_DIR)/fig
CHAP4_PDFTEX_DIR=$(CHAP4_DIR)/pdftex
CHAP4_PDFTEX_T_DIR=$(CHAP4_DIR)/pdftex_t

CHAP5_DIR=Chapitre_5
CHAP5_XFIG_DIR=$(CHAP5_DIR)/fig
CHAP5_PDFTEX_DIR=$(CHAP5_DIR)/pdftex
CHAP5_PDFTEX_T_DIR=$(CHAP5_DIR)/pdftex_t

CHAP6_DIR=Chapitre_6
CHAP6_XFIG_DIR=$(CHAP6_DIR)/fig
CHAP6_PDFTEX_DIR=$(CHAP6_DIR)/pdftex
CHAP6_PDFTEX_T_DIR=$(CHAP6_DIR)/pdftex_t

PDFFMT=pdf

MAIN=Main

.PHONY : all
all : pdf

.PHONY : show
show : $(MAIN).pdf
	evince $< &

SUFFIXES : .tex .fig .pdftex .pdftex_t .pdf

vpath %.fig $(MAIN_XFIG_DIR)
vpath %.pdf $(MAIN_PDFTEX_DIR)
vpath %.pdftex_t $(MAIN_PDFTEX_T_DIR)

main_fig_files          := $(notdir $(shell ls $(MAIN_XFIG_DIR)/*.fig))
main_fig2pdftex_files   := $(main_fig_files:%.fig=%.pdf)
main_fig2pdftex_t_files := $(main_fig_files:%.fig=%.pdftex_t)

chap1_fig_files          := $(shell ls $(CHAP1_XFIG_DIR)/*.fig)
chap1_fig2pdftex_files   := $(chap1_fig_files:%.fig=%.pdf)
chap1_fig2pdftex_t_files := $(chap1_fig_files:%.fig=%.pdftex_t)

$(info "DEBUG : chap1_fig_files is " $(chap1_fig_files))
$(info "DEBUG : chap1_fig2pdftex_files is " $(chap1_fig2pdftex_files))
$(info "DEBUG : chap1_fig2pdftex_t_files is " $(chap1_fig2pdftex_t_files))

chap2_fig_files          := $(shell ls $(CHAP2_XFIG_DIR)/*.fig)
chap2_fig2pdftex_files   := $(chap2_fig_files:%.fig=%.pdf)
chap2_fig2pdftex_t_files := $(chap2_fig_files:%.fig=%.pdftex_t)

chap3_fig_files          := $(shell ls $(CHAP3_XFIG_DIR)/*.fig)
chap3_fig2pdftex_files   := $(chap3_fig_files:%.fig=%.pdf)
chap3_fig2pdftex_t_files := $(chap3_fig_files:%.fig=%.pdftex_t)

chap4_fig_files          := $(shell ls $(CHAP4_XFIG_DIR)/*.fig)
chap4_fig2pdftex_files   := $(chap4_fig_files:%.fig=%.pdf)
chap4_fig2pdftex_t_files := $(chap4_fig_files:%.fig=%.pdftex_t)

chap5_fig_files          := $(shell ls $(CHAP5_XFIG_DIR)/*.fig)
chap5_fig2pdftex_files   := $(chap5_fig_files:%.fig=%.pdf)
chap5_fig2pdftex_t_files := $(chap5_fig_files:%.fig=%.pdftex_t)

chap6_fig_files          := $(shell ls $(CHAP6_XFIG_DIR)/*.fig)
chap6_fig2pdftex_files   := $(chap6_fig_files:%.fig=%.pdf)
chap6_fig2pdftex_t_files := $(chap6_fig_files:%.fig=%.pdftex_t)


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
	$(RM) $(MAIN).pdf
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
	$(RM) -r $(MAIN_PDFTEX_DIR) $(MAIN_PDFTEX_T_DIR)  \
		$(CHAP1_PDFTEX_DIR) $(CHAP1_PDFTEX_T_DIR) \
		$(CHAP2_PDFTEX_DIR) $(CHAP2_PDFTEX_T_DIR) \
		$(CHAP3_PDFTEX_DIR) $(CHAP3_PDFTEX_T_DIR) \
		$(CHAP4_PDFTEX_DIR) $(CHAP4_PDFTEX_T_DIR) \
		$(CHAP5_PDFTEX_DIR) $(CHAP5_PDFTEX_T_DIR) \
		$(CHAP6_PDFTEX_DIR) $(CHAP6_PDFTEX_T_DIR) \
		${CHAP1_DIR}/auto   ${CHAP2_DIR}/auto     \
		${CHAP3_DIR}/auto   ${CHAP4_DIR}/auto     \
		${CHAP5_DIR}/auto   ${CHAP6_DIR}/auto     \
.PHONY : pdf
pdf : $(MAIN).pdf

$(MAIN).pdf : $(MAIN).tex pictures
	pdflatex $<
	bibtex $(MAIN)
	pdflatex $<
	pdflatex $<

#bibtex $(MAIN)

.PHONY : pictures
pictures : main_pictures chap1_pictures chap2_pictures chap3_pictures chap4_pictures chap5_pictures chap6_pictures

# Rules to build main pictures only
.PHONY : main_pictures
main_pictures : main_fig2pdftex_t main_fig2pdftex

main_fig2pdftex_t : $(main_fig2pdftex_t_files)
main_fig2pdftex   : $(main_fig2pdftex_files)

${main_fig2pdftex_t_files} : $(notdir ${main_fig_files})
	test ! -d pdftex_t && mkdir -p pdftex_t || echo -n
	fig2dev -L pdftex_t  -l landscape \
	-p "\pdfteximgpath/"$(notdir $(basename ($(@)))).pdf	  $< \
	$(MAIN_PDFTEX_T_DIR)/$(notdir $(@))

${main_fig2pdftex_files} : $(notdir ${main_fig_files})
	test ! -d pdftex && mkdir -p pdftex || echo -n
	fig2dev -L pdftex -l landscape $< $(MAIN_PDFTEX_DIR)/$(notdir $(@))

# Rules to build chap1 pictures only
.PHONY : chap1_pictures
chap1_pictures : chap1_fig2pdftex_t chap1_fig2pdftex

chap1_fig2pdftex_t : $(chap1_fig2pdftex_t_files)
chap1_fig2pdftex   : $(chap1_fig2pdftex_files)

${chap1_fig2pdftex_t_files} : ${chap1_fig_files}
	test ! -d ${CHAP1_DIR}/pdftex_t && mkdir -p ${CHAP1_DIR}/pdftex_t || echo -n
	fig2dev -L pdftex_t  -l landscape \
	-p "\chaponepdfteximgpath/"$(notdir $(basename ($(@)))).pdf	$(basename $(@)).fig \
	$(CHAP1_PDFTEX_T_DIR)/$(notdir $(@))

${chap1_fig2pdftex_files}  : ${chap1_fig_files}
	test ! -d ${CHAP1_DIR}/pdftex && mkdir -p ${CHAP1_DIR}/pdftex || echo -n
	fig2dev -L pdftex -l landscape $(basename $(@)).fig $(CHAP1_PDFTEX_DIR)/$(notdir $(@))

# Rules to build chap2 pictures only
.PHONY : chap2_pictures
chap2_pictures : chap2_fig2pdftex_t chap2_fig2pdftex

chap2_fig2pdftex_t : $(chap2_fig2pdftex_t_files)
chap2_fig2pdftex   : $(chap2_fig2pdftex_files)

${chap2_fig2pdftex_t_files} : ${chap2_fig_files}
	test ! -d ${CHAP2_DIR}/pdftex_t && mkdir -p ${CHAP2_DIR}/pdftex_t || echo -n
	fig2dev -L pdftex_t  -l landscape \
	-p "\chaptwopdfteximgpath/"$(notdir $(basename ($(@)))).pdf	$(basename $(@)).fig \
	$(CHAP2_PDFTEX_T_DIR)/$(notdir $(@))

${chap2_fig2pdftex_files}  : ${chap2_fig_files}
	test ! -d ${CHAP2_DIR}/pdftex && mkdir -p ${CHAP2_DIR}/pdftex || echo -n
	fig2dev -L pdftex -l landscape $(basename $(@)).fig $(CHAP2_PDFTEX_DIR)/$(notdir $(@))

# Rules to build chap3 pictures only
.PHONY : chap3_pictures
chap3_pictures : chap3_fig2pdftex_t chap3_fig2pdftex

chap3_fig2pdftex_t : $(chap3_fig2pdftex_t_files)
chap3_fig2pdftex   : $(chap3_fig2pdftex_files)

${chap3_fig2pdftex_t_files} : ${chap3_fig_files}
	test ! -d ${CHAP3_DIR}/pdftex_t && mkdir -p ${CHAP3_DIR}/pdftex_t || echo -n
	fig2dev -L pdftex_t  -l landscape \
	-p "\chapthreepdfteximgpath/"$(notdir $(basename ($(@)))).pdf	$(basename $(@)).fig \
	$(CHAP3_PDFTEX_T_DIR)/$(notdir $(@))

${chap3_fig2pdftex_files}  : ${chap3_fig_files}
	test ! -d ${CHAP3_DIR}/pdftex && mkdir -p ${CHAP3_DIR}/pdftex || echo -n
	fig2dev -L pdftex -l landscape $(basename $(@)).fig $(CHAP3_PDFTEX_DIR)/$(notdir $(@))

# Rules to build chap4 pictures only
.PHONY : chap4_pictures
chap4_pictures : chap4_fig2pdftex_t chap4_fig2pdftex

chap4_fig2pdftex_t : $(chap4_fig2pdftex_t_files)
chap4_fig2pdftex   : $(chap4_fig2pdftex_files)

${chap4_fig2pdftex_t_files} : ${chap4_fig_files}
	test ! -d ${CHAP4_DIR}/pdftex_t && mkdir -p ${CHAP4_DIR}/pdftex_t || echo -n
	fig2dev -L pdftex_t  -l landscape \
	-p "\chapfourpdfteximgpath/"$(notdir $(basename ($(@)))).pdf	$(basename $(@)).fig \
	$(CHAP4_PDFTEX_T_DIR)/$(notdir $(@))

${chap4_fig2pdftex_files}  : ${chap4_fig_files}
	test ! -d ${CHAP4_DIR}/pdftex && mkdir -p ${CHAP4_DIR}/pdftex || echo -n
	fig2dev -L pdftex -l landscape $(basename $(@)).fig $(CHAP4_PDFTEX_DIR)/$(notdir $(@))

# Rules to build chap5 pictures only
.PHONY : chap5_pictures
chap5_pictures : chap5_fig2pdftex_t chap5_fig2pdftex

chap5_fig2pdftex_t : $(chap5_fig2pdftex_t_files)
chap5_fig2pdftex   : $(chap5_fig2pdftex_files)

${chap5_fig2pdftex_t_files} : ${chap5_fig_files}
	test ! -d ${CHAP5_DIR}/pdftex_t && mkdir -p ${CHAP5_DIR}/pdftex_t || echo -n
	fig2dev -L pdftex_t  -l landscape \
	-p "\chapfivepdfteximgpath/"$(notdir $(basename ($(@)))).pdf	$(basename $(@)).fig \
	$(CHAP5_PDFTEX_T_DIR)/$(notdir $(@))

${chap5_fig2pdftex_files}  : ${chap5_fig_files}
	test ! -d ${CHAP5_DIR}/pdftex && mkdir -p ${CHAP5_DIR}/pdftex || echo -n
	fig2dev -L pdftex -l landscape $(basename $(@)).fig $(CHAP5_PDFTEX_DIR)/$(notdir $(@))

# Rules to build chap6 pictures only
.PHONY : chap6_pictures
chap6_pictures : chap6_fig2pdftex_t chap6_fig2pdftex

chap6_fig2pdftex_t : $(chap6_fig2pdftex_t_files)
chap6_fig2pdftex   : $(chap6_fig2pdftex_files)

${chap6_fig2pdftex_t_files} : ${chap6_fig_files}
	test ! -d ${CHAP6_DIR}/pdftex_t && mkdir -p ${CHAP6_DIR}/pdftex_t || echo -n
	fig2dev -L pdftex_t  -l landscape \
	-p "\chapsixpdfteximgpath/"$(notdir $(basename ($(@)))).pdf	$(basename $(@)).fig \
	$(CHAP6_PDFTEX_T_DIR)/$(notdir $(@))

${chap6_fig2pdftex_files}  : ${chap6_fig_files}
	test ! -d ${CHAP6_DIR}/pdftex && mkdir -p ${CHAP6_DIR}/pdftex || echo -n
	fig2dev -L pdftex -l landscape $(basename $(@)).fig $(CHAP6_PDFTEX_DIR)/$(notdir $(@))

# Ancienne méthode, tout build d'un coup :

# %.pdftex_t : %.fig
# 	test ! -d pdftex_t && mkdir -p pdftex_t || echo -n
# 	fig2dev -L pdftex_t  -l landscape \
# 	-p "\pdfteximgpath/"$*.pdf	  $< \
# 	$(MAIN_PDFTEX_T_DIR)/$(notdir $(@))

# 	# test ! -d ${CHAP2_DIR}/pdftex_t && mkdir -p ${CHAP2_DIR}/pdftex_t || echo -n
# 	# fig2dev -L pdftex_t  -l landscape \
# 	# -p "\pdfteximgpath/"$*.pdf	  $< \
# 	# $(CHAP2_PDFTEX_T_DIR)/$(notdir $(@))

# %.pdf : %.fig
# 	test ! -d pdftex && mkdir -p pdftex || echo -n
# 	fig2dev -L pdftex -l landscape $< $(MAIN_PDFTEX_DIR)/$(notdir $(@))

# 	# test ! -d ${CHAP2_DIR}/pdftex && mkdir -p ${CHAP2_DIR}/pdftex || echo -n
# 	# fig2dev -L pdftex -l landscape $< $(CHAP2_PDFTEX_DIR)/$(notdir $(@))




# end
