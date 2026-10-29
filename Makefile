
codecheck:  ## Run code check (Ruff, Black and isort)
	@uv run black . -l 79 --check --skip-string-normalization
	@uv run isort . --line-length 79 --multi-line 3 --trailing-comma --check-only
	@uv run ruff check .
