Install all dependencies using
```commandline
pip install -r requirements.txt
```
` python -m pytest tests/ -m login`
` pytest -m login -sv`
` pytest -m login`
allure generate allure-results --clean -o allure-report allure serve allure-results