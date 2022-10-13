info:
	@echo "Makefile is your friend"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

serve: ## serve app
	npx @11ty/eleventy --serve

build: ## build app
	npx @11ty/eleventy

build-netlify: ## build command to deploy on netlify
    eleventy