BIN = /usr/local/bin
SRC = $(PWD)/src

all: install link

install:
	pip install -r requirements.txt

link:
	ln -sf "$(SRC)/start.py" "$(BIN)/dwm-status-bar"

unlink:
	if test -L "$(BIN)/dwm-status-bar"; then \
		dwm-status-bar close; \
		rm "$(BIN)/dwm-status-bar"; \
	fi

.PHONY: all install link unlink
