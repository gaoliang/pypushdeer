import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypushdeer",
    version="0.0.3",
    author="Gao Liang",
    author_email="gaoliangim@gmail.com",
    description="PushDeer for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/gaoliang/pypushdeer",
    project_urls={
        "Bug Tracker": "https://github.com/gaoliang/pypushdeer/issues",
    },
    install_requires=["requests>=2.25.1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.5",
)
