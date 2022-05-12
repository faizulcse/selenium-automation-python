from setuptools import setup

setup(
    name='selenium-automation-python',
    version='1.0.0',
    packages=['src', 'src.pages', 'src.tests'],
    url='',
    license='MIT license',
    author='Faizul Islam',
    author_email='faizulcse@gmail.com',
    description='A prototype of selenium-automation-python',
    install_requires=['selenium', 'webdriver-manager', 'pytest', 'pytest-dotenv',
                      'pytest-xdist', 'allure-pytest', 'pytest-cov', 'pytest-html']
)
