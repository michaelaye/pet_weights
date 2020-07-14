from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="pet_weights",
    version="0.1.0",
    description="Simple CLI to store pet weights in a CSV file.",
    long_description=long_description,
    url="https://github.com/michaelaye/pet_weights",
    author="Michael Aye",
    author_email="kmichael.aye@gmail.com",
    py_modules=["pet_weights"],
    python_requires=">=3.7, <4",
    install_requires=["pandas", "fire"],
    entry_points={"console_scripts": ["pet_weights=pet_weights:main"]},
)
