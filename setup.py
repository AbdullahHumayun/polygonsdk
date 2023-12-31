from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='fudstop',
    version='1.12',
    author='Chuck Dustin',
    author_email='chuckdustin12@gmail.com',
    description='Utilize several market-data APIs in production-ready format for real-time and simulated market analysis.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chuckdustin12/polygonsdk',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='trading, stocks, options, crypto, forex, indices, discord',
)

