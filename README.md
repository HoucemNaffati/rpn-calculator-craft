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
