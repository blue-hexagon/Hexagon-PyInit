# Python Giggle
Fast and easy setup of various utilities and formatters.

Copy over the following files into your new project:
- `.gitignore`
- `setup.cfg`
- `pyproject.toml` - Modify `target-version = ['py310']` with your own version
- `.pre-commit-config.yaml`
- `LICENSE` (if you wish to add the MIT license)

# Setup
- Initialize Git
- pip install pre-commit pytest pytest-cov
- pre-commit install
- pre-commit autoupdate

Now you have successfully setup the following tools:
- `pre-commit`
- `black`
- `flake8`
- `mypy`
- `isort`

All that's left is running:
`pre-commit run --all-files`
