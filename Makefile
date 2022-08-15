BIN="${HOME}/.local/bin"

default:
	cat instructions.txt

install:
	pip install -r requirements.txt

link:
	ln -sf "${PWD}/output.py" "$(BIN)/dwm-status-bar"
	ln -sf "${PWD}/cpu.py" "$(BIN)/status-bar-cpu"
	ln -sf "${PWD}/ram.py" "$(BIN)/status-bar-ram"
	ln -sf "${PWD}/disk.py" "$(BIN)/status-bar-disk"
	ln -sf "${PWD}/battery.py" "$(BIN)/status-bar-battery"
