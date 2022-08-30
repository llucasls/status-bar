BIN = ${HOME}/.local/bin
SRC = ${PWD}/src

default:
	cat instructions.txt

install:
	pip install -r requirements.txt

link:
	ln -sf "$(SRC)/start.py" "$(BIN)/dwm-status-bar"

unlink:
	killall python
	xsetroot -name ""
	if test -L "$(BIN)/dwm-status-bar"; then rm "$(BIN)/dwm-status-bar"; fi
