
codecheck:  ## Run code check (flake8, black and isort)
	@flake8 .
	@black . -l 79 --check --skip-string-normalization
	@isort . -rc -l 79 -m 3 -tc --check-only
	@unify --check-only --recursive ./*
