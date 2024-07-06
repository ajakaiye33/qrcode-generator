# Define the directories and files
SRC_DIR := src utils tests
CONFIG_DIR := config
CONFIG_FILE := $(CONFIG_DIR)/config.json
REQUIREMENTS := requirements.txt
DOCKER_IMAGE := myapp:latest

install:
	# Install commands
	pip install --upgrade pip && \
		pip install -r $(REQUIREMENTS)

format:
	# Format code
	black $(SRC_DIR)/*.py $(SRC_DIR)/*.py ./*.py

lint:
	# Lint code
	pylint --disable=R,C,broad-except $(SRC_DIR)/*.py $(SRC_DIR)/*.py

test:
	# Run tests
	#pytest

build:
	# Build container
	#docker build -t $(DOCKER_IMAGE) .

run:
	# Run container
	#docker run -v $(shell pwd):/app -p 8501:8501 $(DOCKER_IMAGE)

deploy:
	# Deploy commands
	# Add your deployment commands here

generate:
	# Generate QR Codes
	python app.py --config config/config.json --output ./output

all: install format lint test
