# RPN Calculator


## How to install?

* `make configure`: this will prepare your environment using venv, python3 and flit.

For development : `make install-dev` as it will enable editable installation.   
For production  : `make install`

## How to run?

start in interactive mode: `make run`
swagger is on http://localhost:8000/docs

## How to test?

For running all tests:

`make test`

For running only unit tests:

`make test-unit`

For running tests with coverage:

`make test-cov`

## TODOs
* adapt project structure to a light cqrs version and init primary architecture
* implement command pattern with a simple command Bus, each operand is a command, implement command handlers using TDD and DDD patterns
* dockerize for production
* implement real database adapters for production
* add integration test using test containers
* add documentation about project structure and architecture
* add documentation about pre-commit hooks and explain the magic

## Sandbox  suggestions
