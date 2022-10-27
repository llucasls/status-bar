BIN = /usr/local/bin
SRC = ${CURDIR}/src

all: install link

install:
	pip install -r requirements.txt

link:
	ln -sf "$(SRC)/start.py" "$(BIN)/dwm-status-bar"

unlink:
	killall python
	if test -L "$(BIN)/dwm-status-bar"; then rm "$(BIN)/dwm-status-bar"; fi
