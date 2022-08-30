BIN = ${HOME}/.local/bin
SRC = ${PWD}/src

default:
	cat instructions.txt

install:
	pip install -r requirements.txt

link:
	ln -sf "$(SRC)/start.py" "$(BIN)/dwm-status-bar"
