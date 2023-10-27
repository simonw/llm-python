# llm-python

[![PyPI](https://img.shields.io/pypi/v/llm-python.svg)](https://pypi.org/project/llm-python/)
[![Changelog](https://img.shields.io/github/v/release/simonw/llm-python?include_prereleases&label=changelog)](https://github.com/simonw/llm-python/releases)
[![Tests](https://github.com/simonw/llm-python/workflows/Test/badge.svg)](https://github.com/simonw/llm-python/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/llm-python/blob/main/LICENSE)

Run a Python interpreter in the LLM virtual environment

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).

    llm install llm-python

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-python
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
pytest
```
