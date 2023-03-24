BIN = /usr/local/bin
SRC = $(CURDIR)/src

PYTHON = python3
PIP = $(PYTHON) -m pip

all: install link

install:
	$(PIP) install -r requirements.txt

link:
	ln -sf "$(SRC)/start.py" "$(BIN)/dwm-status-bar"

unlink:
	if test -L "$(BIN)/dwm-status-bar"; then \
		dwm-status-bar close; \
		rm "$(BIN)/dwm-status-bar"; \
	fi

.PHONY: all install link unlink
