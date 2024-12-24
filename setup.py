import setuptools

with open("README.md","r",encoding="utf-8") as f:
    log_description = f.read()

__version__ = "0.0.0.0"

REPO_NAME = "XAI-SENTIMENTANALYSIS"
AUTHOR_USER_NAME = "GyanendraChaubey"
SRC_REPO = "XAI_SentimentAnalysis"
AUTHOR_EMAIL = "gyanendrachaubey68@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for implementing sentiment analysis using XAI",
    log_description=log_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Trackers" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    )