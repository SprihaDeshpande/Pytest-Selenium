from selenium import webdriver
from time import sleep
import re

from test_locators import Locator

'''
Intial Test set up - add executable path for chromedriver and get the application for GAME
And maximize the browser
'''
def test_setup():
    global chrome_driver
    chrome_driver = webdriver.Chrome(executable_path=r'/Users/sprihad/Downloads/chromedriver')
    chrome_driver.get('http://ec2-54-208-152-154.compute-1.amazonaws.com/')
    chrome_driver.maximize_window()

'''
Testing board game logic
1. Retrieve the coin elements and store in available_coins and their values in available_coins_value
2. Since we are using two pointers that covers elements simultaneously, we run a while loop until
 iterative_count < (len(available_coins)//2)
3. The right and left board will be populated with values from pointers pointing to coins and their own value indexes
4. Increment the pointer and find if resultant has "=" operator.
5. if "=" operator is present in result weighings, continue the while loop, else break the loop
6. Return the last value of the stack which caused this condition of the stack which is lesser in weight
7. Locate the uneven element in the coin stack and click it to find an alert pop up. 
8. Verify "Yay! You find it!" string is present in pop up.
'''
def test_game():
    available_coins = chrome_driver.find_elements_by_xpath(Locator.locators["available_coins"])
    global available_coins_value
    available_coins_value = []

    for i in range(len(available_coins)-1, -1, -1):
        available_coins_value.append(available_coins[i].text)

    first_pointer = 0
    second_pointer = 1
    operator_flag = True
    iterative_count = 0
    while iterative_count < (len(available_coins)//2):
        chrome_driver.find_elements_by_xpath(Locator.locators["left_board"])[first_pointer].send_keys(available_coins_value.pop())
        first_pointer += 2
        sleep(1)
        chrome_driver.find_elements_by_xpath(Locator.locators["right_board"])[second_pointer].send_keys(available_coins_value.pop())
        second_pointer += 2
        sleep(1)

        chrome_driver.find_element_by_xpath(Locator.locators["weight_button"]).click()
        sleep(1)

        weighing_outcome = chrome_driver.find_elements_by_xpath(Locator.locators["weighings"])[iterative_count].text
        if "=" not in weighing_outcome:
            operator_flag = False
            break
        iterative_count+=1

    if operator_flag:
        uneven_element = available_coins_value.pop()
    else:
        if "<" in weighing_outcome:
            uneven_element = re.match(r'.*(\d)].*<',weighing_outcome).group(1)
        elif ">" in weighing_outcome:
            uneven_element = re.match(r'.*>.*(\d)].*',weighing_outcome).group(1)

    available_coins[int(uneven_element)].click()
    alert_obj = chrome_driver.switch_to.alert
    sleep(1)
    assert "Yay! You find it!" in alert_obj.text
    sleep(1)
    alert_obj.accept()
    sleep(1)

'''
Testing reset funtion
1. iterate through every element in available coins
2. Value of coin index is the index of the board games
3. Even numbers are designated to left board and odd numbers are designated to right board
'''
def test_reset():
    chrome_driver.find_element_by_xpath(Locator.locators["reset_button"]).click()
    sleep(1)

    for i in available_coins_value:
        if int(i)%2 == 0:
            assert chrome_driver.find_elements_by_xpath(Locator.locators["left_board"])[int(i)].get_attribute("value") == ""
        else:
            assert chrome_driver.find_elements_by_xpath(Locator.locators["right_board"])[int(i)].get_attribute("value") == ""
'''
Close the window after testing is complete.
'''
def test_teardown():
    chrome_driver.close()
    print("Test is Complete")
