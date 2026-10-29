
codecheck:  ## Run code check (flake8, black and isort)
	@uv run flake8 .
	@uv run black . -l 79 --check --skip-string-normalization
	@uv run isort . --line-length 79 --multi-line 3 --trailing-comma --check-only
	@uv run ruff check . --select Q
