# RPN Calculator


## How to install?

* `make configure`: this will prepare your environment using venv, python3 and flit.

For development : `make install-dev` as it will enable editable installation.   
For production  : `make install`

## How to run?

start in interactive mode: `make run`
swagger is on http://localhost:8000/docs

## What happens when I commit code?

## How to test?

For running all tests:

`make test`

For running only unit tests:

`make test-unit`

For running tests with coverage:

`make test-cov`


## Architecture 
Hexagonal architecture
CQRS (light)

## Patterns
Command
Repository
Aggregate

## Methodology
Use case driven
TDD
DDD
Test First
Pyramid of tests with outside in approach (Chicago school)

Find more information about VisionPM (my company) approach and culture,
check out this software craftsmanship KATA I've created few years
ago [here](https://houcemnaffati.github.io/A-Software-Craftsmanship-KATA/):
