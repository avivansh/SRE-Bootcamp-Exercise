# Makefile
all: permission env_up


permission:
	@chmod +x docker-entrypoint.sh

env_up: .env
	@docker-compose build
	@docker-compose up

.env:
	@cat .env-example > .env
