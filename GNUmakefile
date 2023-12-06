BIN = /usr/local/bin
SRC = $(CURDIR)/src

PYTHON = python3
PIP = $(PYTHON) -m pip

all: install link

install:
	$(MAKE) --no-print-directory -f config.mk install

link: | $(BIN)
	ln -sf "$(SRC)/start.py" "$(BIN)/dwm-status-bar"

$(BIN):
	mkdir -p $@

unlink:
	if test -L "$(BIN)/dwm-status-bar"; then
		dwm-status-bar close
		rm "$(BIN)/dwm-status-bar"
	fi

.PHONY: all install link unlink

.ONESHELL:
