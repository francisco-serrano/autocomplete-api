# these commands are meant to be run within docker DEV container

test:
	pytest

build:
	python /app/autocomplete_build.py

run:
	python /app/autocomplete_server.py
