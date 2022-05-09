### Setup environment and install all dependencies

- Go to project root directory and run the following command
- `python setup.py install`

### Run the test cases using following commands

- ` python -m pytest tests/ -m login`
- ` pytest -m login -sv`
- ` pytest -m login`
- `allure generate allure-results --clean -o allure-report allure serve allure-results`