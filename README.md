### Setup environment and install all dependencies

- Go to project root directory and run the following command
- `python setup.py install`

### Run the test cases using following commands

- ` pytest src/tests/ -q`
- ` pytest src/tests/ -vq`
- ` pytest src/tests/ -m login -sv`
- ` pytest -m login -q`
- `allure generate allure-results --clean -o allure-report allure serve allure-results`