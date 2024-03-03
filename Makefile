# Makefile
all: env_up

env_up: .env
	@docker-compose up

.env:
	@cat .env-example > .env

.PHONY: all env_up
