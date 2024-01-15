from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="numero_a_letras",
    version="0.0.4",
    description="Convierte un número a letras en español",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lugezz/numero_a_letras_literal",
    author="Eugenio",
    author_email="coding_with@eugeniovazquez.com.ar",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        # Optional
        # e.g "numpy==1.11.1", "tensorflow>=1.1.0"
    ],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.10, <3.12",
)
