# Python string inverter

[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

This module/library is to invert the given string

## Test
---
This uses [pytest](https://pypi.org/project/pytest/) to run unit tests and generate the report.
Uses the pytest version [5.3.5](https://pypi.org/project/pytest/5.3.5/).

Below are the test cases
| **Test case**                           | **Input** | **Expected Output** |
|-----------------------------------------|-----------|---------------------|
| Test with valid input string            | Hello     | olleH               | 
| Test with empty input string            |           |                     |
| Test with None input string             | None      |                     |
| Test with single char input string      | A         |   A                 |

## GitHub Action Workflow
---
This can be tested with running the GitHub action [workflow](https://github.com/kumvijaya/py-string-inverter/actions/workflows/build.yml). This runs and publishes the test results in job summary.

## Local testing
---
This sample can be cloned in local, and run using below command with python 3.8.

```
python -m pytest
```

## License
---
[Internal]
