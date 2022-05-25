EXE="dathomir"
VERSION="1.0.0"
.PHONY: run

all: run

# Run program
run:
	python main.py

run-debug:
	python main.py --debug

run-console:
	python main.py --console

run-console-debug:
	python main.py --console --debug

# Run test all
test:
	python -m unittest

# venv activate
venv:
	source .venv/bin/activate

# Handle modules
# list-modules:
# 	pip freeze

update-modules:
	pip freeze > requirements.txt

install-modules:
	pip install -r requirements.txt

list-modules:
	pip freeze

uninstall-modules:
	pip uninstall -y -r <(pip freeze)

# list all target in makefile
list:
	@grep '^[^#[:space:]].*:' Makefile | grep -v '\.PHONY'