VENV_DIR ?= .venv
TEST_DIR ?= tests

PACKAGE_NAME = app

.PHONY: uv-installed
uv-installed:
	@command -v uv &> /dev/null ||\
		(echo "UV doesn't seem to be installed, try the following instructions:" &&\
		echo "https://docs.astral.sh/uv/getting-started/installation/" && false)

.PHONY: clean-caches
clean-caches:
	@rm -rf .pytest_cache *.egg-info
	@find . -type d -name "__pycache__" -prune -print -exec rm -rf {} +
	@rm uv.lock

.PHONY: venv
venv: uv-installed
	uv sync

.PHONY: clean
clean: clean-caches
	@rm -rf ${VENV_DIR}
	@rm *.db

.PHONY: pytest
pytest: uv-installed
	uv run pytest ${TEST_DIR} -W error -vv

.PHONY: serve
serve: uv-installed
	uv run uvicorn main:app --reload --port 8080

.PHONY: create
create: uv-installed
	curl -X 'POST' \
	  'http://localhost:8080/products/hello/world' \
	  -H 'accept: application/json' \
	  -d ''
	

.PHONY: list
list: uv-installed
	curl -X 'GET' \
	  'http://localhost:8080/products' \
	  -H 'accept: application/json'


.PHONY: delete-all
delete-all: uv-installed
	curl -X 'DELETE' \
	  'http://localhost:8080/delete_all' \
	  -H 'accept: application/json'


.PHONY: tag
tag: uv-installed
	curl -X 'GET' \
	  'http://localhost:8080/tags/1' \
	  -H 'accept: application/json'
