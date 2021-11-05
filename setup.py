import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="antidist",
    version="1.0",
    author="Vincent Russo",
    author_email="vincentrusso1@gmail.com",
    description="Python code for the antidistinguishability conjecture.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vprusso/antidist",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
