from setuptools import setup, find_packages

setup(
    name="ecommerce_analyzer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python"
    ],
    entry_points={
        "console_scripts": [
            "ecommerce_analyzer = ecommerce_analyzer.__main__:main"
        ]
    }
)
