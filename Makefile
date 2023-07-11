PHONY: start-local
start-local:
	docker-compose up -d
	sleep 10

PHONY: stop-local
stop-local:
	docker-compose down

PHONY: build-local
build-local:
	docker-compose build
