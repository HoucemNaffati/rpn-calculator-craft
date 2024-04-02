PYTHON=./.venv/bin/python

.PHONY = help install install-dev test test-cov format lint type-check secure run

configure:
	@echo "Configuring your environment using venv, python3 (should be installed) and flit"
	python3 -m venv .venv && \
	source .venv/bin/activate && \
	pip install flit==3.9.0
help:
	@echo "---------------HELP-----------------"
	@echo "To install the project -> make install"
	@echo "To install the project for development -> make install-dev"
	@echo "To test the project -> make test"
	@echo "To test with coverage -> make test-cov"
	@echo "To format code -> make format"
	@echo "To check linter -> make lint"
	@echo "To run type checker -> make type-check"
	@echo "To run all security related commands -> make secure"
	@echo "To run the web server -> make run"
	@echo "------------------------------------"

install:
	${PYTHON} -m flit install --env --deps=production

install-dev:
	${PYTHON} -m flit install --env --deps=develop --symlink && pre-commit install

test-unit:
	TEST_RUN="TRUE" ${PYTHON} -m pytest -svvv  -m unit tests

test:
	TEST_RUN="TRUE" ${PYTHON} -m pytest -svvv  tests

test-cov:
	TEST_RUN="TRUE" ${PYTHON} -m pytest -svvv --cov-report html --cov=src tests

format:
	${PYTHON} -m isort src tests --force-single-line-imports
	${PYTHON} -m autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py
	${PYTHON} -m black src tests --config pyproject.toml
	${PYTHON} -m isort src tests

lint:
	${PYTHON} -m flake8 src
	${PYTHON} -m black src tests --check --diff --config pyproject.toml
	${PYTHON} -m isort src tests --check --diff

type-check:
	${PYTHON} -m pytype --config=pytype.cfg src

secure:
	${PYTHON} -m bandit -r src --config pyproject.toml

run:
	${PYTHON} -m uvicorn src.rpn_calculator.web.main:app --host 0.0.0.0 --port 8000 --reload