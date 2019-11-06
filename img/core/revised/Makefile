CONVERT=convert

PNG_FILES := $(wildcard *.png)
JPG_FILES := $(wildcard *.jpg)
PNG_EPS_FILES := $(PNG_FILES:%.png=%.eps)
JPG_EPS_FILES := $(JPG_FILES:%.jpg=%.eps)

all: eps

eps: $(PNG_EPS_FILES) $(JPG_EPS_FILES)

%.eps: %.png
	$(CONVERT) $< $@

%.eps: %.jpg
	$(CONVERT) $< $@

.PHONY: clean

clean: $(PNG_EPS_FILES) $(JPG_EPS_FILES)
	rm -rf $(PNG_EPS_FILES) $(JPG_EPS_FILES)

