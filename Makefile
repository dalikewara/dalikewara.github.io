info:
	@echo "Makefile is your friend"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build-netlify: ## build command to deploy on netlify
	@pip3 install mkdocs
	@pip3 install mkdocs-material
	@pip3 install mkdocs-minify-plugin
	@mkdocs build