###########################################################
#          This is an example - must be modified          
###########################################################
# Create a MANIFEST.in
# To include other files
# Add:
# include output README.md LICENSE

###########################################################
import pathlib

from setuptools import find_packages, setup

VERSION = "1.0.52"
NAME = "winscraper"
DESCRIPTION = "A CLI tool and a library used for collecting information about devices running the Windows OS."
WORKING_DIR = pathlib.Path(__file__).parent
README_CONTENT = (WORKING_DIR / "README.md").read_text()
REQUIREMENTS = [
    'psutil==5.8.0',
    'pypiwin32',
    'wmi>=1.5.0',
    'json2xml',
    'toml',
    'pyyaml>=5.4.1',
]
setup(
    name=NAME,
    version=VERSION,
    author="Manjana",
    author_email="w0j8uhv5csio@opayq.net",
    description=DESCRIPTION,
    long_description=README_CONTENT,
    long_description_content_type="text/markdown",
    # options={"bdist_wheel": {"universal": True}},
    url="https://www.github.com/blue-hexagon/winscraper",
    project_urls={
        "Bug Tracker": "https://github.com/blue-hexagon/winscraper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "Topic :: System :: Monitoring",
        "Development Status :: 3 - Alpha",
    ],
    keywords="system monitoring monitor",
    packages=find_packages(),
    python_requires=">=3.9, <4",
    include_package_data=True,
    install_requires=REQUIREMENTS,
    # setup_requires=Anything the setup requires,
    entry_points={
        "console_scripts": [
            "winscraper=src.winscraper:main",
        ]
    },
)
