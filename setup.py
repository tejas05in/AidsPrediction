import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "AidsPrediction"
AUTHOR_USERNAME = "tejas05in"
SRC_REPO = "AidsPrediction"
AUTHOR_EMAIL = "tejas05in@yahoo.co.in"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A simple ml implementation of AidsPrediction project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{SRC_REPO}/issues/",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
