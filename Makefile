PYTHON ?= python3
VENV := venv
PYTHON_BIN := $(VENV)/bin/python
PIP_BIN := $(VENV)/bin/pip
APP := app.py

.PHONY: help venv install run db reset clean

help:
	@echo "Available targets:"
	@echo "  make venv    - create a virtual environment"
	@echo "  make install - install dependencies"
	@echo "  make run     - start the Flask app"
	@echo "  make db      - initialize the SQLite database"
	@echo "  make reset   - delete and recreate the database"
	@echo "  make clean   - remove the virtual environment and cache files"

venv:
	@$(PYTHON) -m venv $(VENV)

install: venv
	@$(PIP_BIN) install --upgrade pip
	@$(PIP_BIN) install flask

run: venv
	@$(PYTHON_BIN) $(APP)

db: venv
	@$(PYTHON_BIN) -c "from database import initialize_database; initialize_database()"

reset: venv
	@rm -f quiz_questions.db
	@$(PYTHON_BIN) -c "from database import initialize_database; initialize_database()"

clean:
	@rm -rf $(VENV) __pycache__
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
