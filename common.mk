export LINTER = flake8 --max-line-length 100
export PYLINTFLAGS = --exclude=__main__.py


PYTHONFILES = $(shell ls *.py)
PYTESTFLAGS = -vv --verbose --cov-branch --cov-report term-missing --tb=short -W ignore::FutureWarning

MAIL_METHOD = api

FORCE:

tests: lint pytests

lint: $(patsubst %.py,%.pylint,$(PYTHONFILES))

%.pylint:
	$(LINTER) $(PYLINTFLAGS) $*.py

pytests: FORCE
	export TEST_DB=1; pytest $(PYTESTFLAGS) --cov=$(PKG)

%.py: FORCE
	$(LINTER) $(PYLINTFLAGS) $@
	export TEST_DB=1; pytest $(PYTESTFLAGS) tests/test_$*.py
