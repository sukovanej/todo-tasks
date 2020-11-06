.PHONY: fix check

fix:
	black src tests
	isort src tests

check:
	mypy src tests

install:
	pip install .
