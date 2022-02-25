# Build & Upload to PyPI
## Testing
```
pip install twine
```

Upload to Test-PyPI:
```
python -m twine upload --repository testpypi dist/*`
```

Test the test-pypi repo with a pip install:
```
pip install -i https://test.pypi.org/simple/ winscraper==1.0.44 --extra-index-url https://upload.pypi.org/legacy/`
```

## Production
Upload to PyPI: `.`

Install from downloaded file: `py -m pip install "Path_of_the_downloaded_file"`

Build: `python -m build`

---
# Building an Executeable
Build Executeable: `pyinstaller winscraper.py`
