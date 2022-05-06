"""Minimal setup file for SELENIUM-AUTOMATION-PYTHON"""
from setuptools import setup, find_packages

setup(
    name='selenium-automation-python',
    version='0.1.0',
    description='Website UI testing using selenium-python',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={},
    # metadata
    author='Faizul Islam',
    author_email='faizulcse@gmail.com',
    license='proprietary',
    install_requires=['selenium', 'webdriver-manager', 'pytest', 'pytest-dotenv',
                      'pytest-xdist', 'allure-pytest', 'pytest-html']
)
