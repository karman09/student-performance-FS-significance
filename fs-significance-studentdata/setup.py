from setuptools import setup, find_packages

setup(
    name="fs-significance-studentdata",
    version="1.0.0",
    description="Feature Selection Significance Analysis on Student Performance Dataset",
    author="Kevser",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "scikit-learn",
        "tabulate",
        "factor-analyzer",
        "xgboost",
    ],
    python_requires=">=3.8",
)
