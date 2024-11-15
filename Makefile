.PHONY: clean clean-pyc clean-test help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -f logs.txt

lint: ## check style with flake8
	flake8 dwolla

format: ## format Python code and check complexity
	@set -e; \
	echo '' && echo 'YAPF formatter...' && \
	yapf -ipr dwolla && echo 'Python complexity check...' && \
	mccabe_failed=0 && \
	for f in $$(find $$(pwd)/dwolla/ -name '*.py';); do \
		output=$$(python3 -m mccabe --min 6 "$$f") && \
		if [ $(strip "$$output") != "" ]; then \
			echo "Too complex: $$f $$output"; \
			mccabe_failed=1; \
		fi; \
	done && \
	if [ $$mccabe_failed -eq 1 ]; then \
		echo '' && exit 1; \
	fi && echo 'pydocstyle...' && echo '' && \
	pydocstyle . && echo 'isort...' && \
	isort . && echo '' && \
	echo 'Format checks complete!' && echo ''

test: ## run tests
	pytest . && exit 0 || \
	coverage report -m --fail-under=100 > /dev/null && exit 1

coverage: ## check code coverage
	@pytest . && exit 0 || \
	coverage report -m > /dev/null || coverage html; \
	$(BROWSER) htmlcov/index.html

deps: ## install dependencies
	pip3 install -r requirements_dev.txt
	pip install -e .
