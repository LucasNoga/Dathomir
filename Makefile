EXE="dathomir"
VERSION="1.1.0"

.PHONY: run
.PHONY: build

# Run program
run:
	python .

run-debug:
	python . --debug

run-console:
	python . --console

run-console-debug:
	python . --console --debug

# Run test all
test-discover:
	python -m unittest discover

test:
	python -m unittest

# Building executable for all OS
build:
	@echo Make sure your are out of virtual env
	@echo Building executable ${EXE}...
	pip install -q pyinstaller
	@echo PyInstaller Version: `pyinstaller --version`
	pyinstaller ${EXE}.py --onedir -y --clean --log-level ERROR
	@cp ./config.example.json ./dist/${EXE}/config.json
	@echo "${EXE} built"

# Test building
build-test:
	@echo Test ${EXE}...
	@cp ./config.example.json ./dist/dathomir/config.json
	@./dist/dathomir/${EXE} --console

# venv activate
venv:
	source .venv/bin/activate

# Handle modules
list-modules:
	pip freeze

update-modules:
	pip freeze > requirements.txt

install-modules:
	pip install -r requirements.txt

uninstall-modules:
	pip uninstall -y -r <(pip freeze)

# list all target in makefile
list:
	@grep '^[^#[:space:]].*:' Makefile | grep -v '\.PHONY'