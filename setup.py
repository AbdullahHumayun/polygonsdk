import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="polygonsdk",
    version="1.0.0",
    author="Chuck",
    author_email="your-email@example.com",
    description="Analyze, query, and fetch market data utilizing Polygon.io's suite of services for simulated and real-time market data analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chuckdustin12/polygonsdk/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List any dependencies your package requires
    ],
)