info:
	@echo "Makefile is your friend"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

serve: ## serve app
	npm run serve

build: ## build app
	npm run build

build-netlify: build ## build command to deploy on netlify

install-debian: ## install nodejs & npx on debian
	curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
	sudo apt update
	sudo apt install nodejs
	npm install