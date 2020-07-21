.DEFAULT: help

help:
	@echo "make build"
	@echo "           build local docker container
	@echo "make run"
	@echo "           start the docker container in interactive mode"
	@echo "make clean"
	@echo "           remove python build and test artifacts  (including output .png files)"


build:
	docker build . \
		-t ee-model \
		--rm=false 

clean: clean-build clean-pyc


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +


clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


run:
	docker run \
		-p 5000:5000 \
		-it ee-model

