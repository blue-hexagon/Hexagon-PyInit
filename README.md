# My PyInit
Fast and easy setup of various utilities and formatters.

Copy over the following files into your new project:
- `.gitignore`
- `setup.cfg`
- `pyproject.toml` - Modify `target-version = ['py310']` with your own version
- `.pre-commit-config.yaml`
- `LICENSE` (if you wish to add the MIT license)

# Setup
- Initialize Git: `git init`
- `poetry add --dev pre-commit pytest pytest-cov pygount taskipy`
- `poetry run pre-commit install`
- `poetry run pre-commit autoupdate`

Now you have successfully setup the following tools:
- `pre-commit` with various hooks
- `black`
- `refurb`
- `flake8`
- `mypy`
- `isort`

All that's left is running:
`poetry run pre-commit run --all-files`

# Tasks
A few tasks are defined and can be run with: `poetry run task <taskname>`
```
pc = { cmd = "pre-commit run --all-files", help = "runs precommit on all files" }
test = { cmd = "pytest", help = "runs all tests" }
test-cov = { cmd = "pytest --cov", help = "runs all tests with coverage" }
test-cov-html = { cmd = "pytest --cov --cov-report html:coverage", help = "runs all tests with coverage and outputs a report found in ./coverage/index.html" }
loc = { cmd = "poetry run pygount ./src --format=summary --suffix=py", help = "Count LOC for the project" }
```
