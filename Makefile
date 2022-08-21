BIN = "${HOME}/.local/bin"
SRC = "${PWD}/src"

default:
	cat instructions.txt

install:
	pip install -r requirements.txt

link:
	ln -sf "$(SRC)/start.py" "$(BIN)/dwm-status-bar"
	ln -sf "$(SRC)/output.py" "$(BIN)/status-bar-output"
	ln -sf "$(SRC)/cpu.py" "$(BIN)/status-bar-cpu"
	ln -sf "$(SRC)/ram.py" "$(BIN)/status-bar-ram"
	ln -sf "$(SRC)/disk.py" "$(BIN)/status-bar-disk"
	ln -sf "$(SRC)/battery.py" "$(BIN)/status-bar-battery"
