from selenium import webdriver
import unittest
import time


class LoginTest(unittest.TestCase):

    def setUp(self):
        chromePath = "C:/Users/tsily/PycharmProjects/pythonProject/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8081/")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def testGoLogin(self):
        driver = self.driver
        self.login("max27@mail.ru", "12345678")
        driver.refresh()
        time.sleep(3)
        self.assertEqual(driver.current_url, "http://localhost:8081/")

    def testNotLogin(self):
        driver = self.driver
        self.login("max27@mail.ru", "12dsa123sasx")
        self.assertEqual(driver.current_url, "http://localhost:8081/login")

    def testNotValidEmailLogin(self):
        driver = self.driver
        self.login("max23.ru", "21232132123")
        self.assertEqual(driver.current_url, "http://localhost:8081/login")

    def testNotValidPasswordLogin(self):
        driver = self.driver
        self.login("max27@mail.ru", "sa123")
        time.sleep(2)
        self.assertEqual(driver.current_url, "http://localhost:8081/login")

    def testRouteProfile(self):
        driver = self.driver
        self.login("max27@mail.ru", "12345678")
        driver.refresh()
        time.sleep(3)
        page = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/main/div/div/div/div[1]/div/div/div[1]/div")
        page.click()
        time.sleep(2)
        item = driver.find_element_by_xpath \
            ("//*[@id=\"app\"]/div/div/main/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]")
        self.assertEqual(item.text, "Максим Цилюрик")

    def login(self, username, password):
        driver = self.driver
        driver.find_element_by_id("emailLogin").send_keys(username)
        driver.find_element_by_id("passwordLogin").send_keys(password)
        buttonReg = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/main/div/div/form/div[3]/button/span")
        buttonReg.click()
        time.sleep(1)
