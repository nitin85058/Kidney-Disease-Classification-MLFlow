import setuptools

with open ('README.md','r',encoding='utf-8') as f:
    long_description=f.read()

__version__="0.0.1"

REPO_NAME="Kidney-Disease-Classification-MLflow"
AUTHOR_USER_NAME="nitin85058projec"
SRC_REPO="cnnclassifier"
AUTHOR_EMAIL="nitinjai85058@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small pytho package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/nitin85058/Kidney-Disease-Classification-MLFlow",
    project_urls={
        "Bug Tracker":f"https://github.com/nitin85058/Kidney-Disease-Classification-MLFlow/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)