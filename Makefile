info:
	@echo "Makefile is your friend"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

serve: ## serve app
	@JEKYLL_ENV=production jekyll serve

serve-watch: ## serve app & watch
	@JEKYLL_ENV=production jekyll serve --watch --livereload

build: ## build app
	@JEKYLL_ENV=production jekyll build

build-netlify: build ## build command to deploy on netlify