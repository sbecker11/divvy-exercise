WORKSPACE?=${shell pwd}
PY_ENV?=venv
VPATH=.:${PY_ENV}/
PYEXE?=python3.6

.PHONY: all
all: clean test

.PHONY: clean
clean:
	-rm -rf ${PY_ENV}

${PY_ENV}:
	${PYEXE} -m venv ${PY_ENV}

build.dev: ${PY_ENV}
	${PY_ENV}/bin/pip install .
	touch ${PY_ENV}/build.dev

.PHONY: test
test: build.dev
	${PY_ENV}/bin/python -m unittest discover tests
