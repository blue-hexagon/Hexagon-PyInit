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
- `poetry add --dev pre-commit pytest pytest-cov`
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
