# Pytest-Selenium Automation 

### Intial installments

1. Make sure to have Pytest Installed by running the command below
`pip install –U pytest`
2. Verify pytest is installed and check version with command below
`pytest --version`
3. Make sure to have Python3.5 or above and pip installed 
Follow the link for Python3 insallations: https://installpython3.com/mac/
Follow the link for PIP installations: https://pip.pypa.io/en/stable/installing/
4. Verify pip installed 
`python -m pip --version`
5. Verify Python installed
`python --version`


### Webdriver installations
1. Install chrome webdriver from the link below
https://chromedriver.chromium.org/downloads
2. Use this Unix executable in the EXACT LOCATION where you are to run the selenium test_selenium.py
3. Change the location of your local webdriver executable in the script of test_selenium.py in test_setup()
4. Provide chromedriver permission to executable for developer verification
`xattr -d com.apple.quarantine chromedriver` 

### Execute 
1. To execute the script test_selenium.py, run the below command
`pytest test_selenium.py`
<img width="1792" alt="Screen Shot 2021-04-18 at 2 04 38 AM" src="https://user-images.githubusercontent.com/50254090/115140100-704a1900-9fea-11eb-8787-0fa022509ba2.png">


