install:
	uv sync

build:
	uv build

lint:
	uv run ruff check

lint-with-fix:
	uv run ruff check --fix

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=algorithms-project-69 --cov-report xml

check: test lint
