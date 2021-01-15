from selenium import webdriver
import unittest
import time


class RegisterTest(unittest.TestCase):

    def setUp(self):
        chromePath = "C:/Users/tsily/PycharmProjects/pythonProject/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8081/")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    # переход на страницу регистрации по ссылке "Зарегестрироваться"
    def testGoReg(self):
        driver = self.driver
        buttonReg = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/main/div/div/form/p[1]/a")
        buttonReg.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://localhost:8081/register")

    def registration(self, name, secondname, email, gender, password):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id=\"nameForm\"]").send_keys(name)
        driver.find_element_by_xpath("//*[@id=\"secondNameForm\"]").send_keys(secondname)
        driver.find_element_by_id("selectRForm").send_keys(gender)
        driver.find_element_by_id("emailRForm").send_keys(email)
        driver.find_element_by_id("formPasswordR").send_keys(password)
        time.sleep(1)
        regButton = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/main/div/div/form/div[6]/button/span")
        regButton.click()
        time.sleep(2)

    def testRegisterUser(self):
        driver = self.driver
        buttonReg = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/main/div/div/form/p[1]/a")
        buttonReg.click()
        self.registration("Max", "Max", "Maxsa2123@mail.ru", "Мужской", "12345678")
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://localhost:8081/login")

    def testNotRegisterUser(self):
        driver = self.driver
        buttonReg = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/main/div/div/form/p[1]/a")
        buttonReg.click()
        self.registration("Max", "Max", "Maxmail.ru", "Мужской", "1278")
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://localhost:8081/register")


