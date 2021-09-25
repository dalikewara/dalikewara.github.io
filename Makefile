info:
	@echo "Makefile is your friend"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## install requirements
	@pip install mkdocs mkdocs-material mkdocs-minify-plugin

serve: ## serve app
	@mkdocs serve

build: ## build app
	@mkdocs build

build-netlify: install build ## build command to deploy on netlify