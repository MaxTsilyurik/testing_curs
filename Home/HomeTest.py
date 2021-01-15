from selenium import webdriver
import unittest
import time


class HomeTest(unittest.TestCase):

    def setUp(self):
        chromePath = "C:/Users/tsily/PycharmProjects/pythonProject/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8081/")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def login(self, username, password):
        driver = self.driver
        driver.find_element_by_id("emailLogin").send_keys(username)
        driver.find_element_by_id("passwordLogin").send_keys(password)
        buttonReg = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/main/div/div/form/div[3]/button/span")
        buttonReg.click()
        time.sleep(1)

    def addPost(self, username, password, text):
        driver = self.driver
        self.login(username, password)
        driver.refresh()
        time.sleep(3)
        item = driver.find_element_by_id("textReadOnly")
        item.click()
        time.sleep(2)
        driver.find_element_by_id("messageFormItem").send_keys(text)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/main/div/div/div/div[2]/div[1]/div[2]/button/span") \
            .click()
        time.sleep(2)
        self.assertEqual(
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/main/div/div/div/div[2]/div[2]/div/div[2]").text,
            text
        )

    def testCreateNewPost(self):
        driver = self.driver
        self.addPost("max27@mail.ru", "12345678", "пост для теста")
        self.assertEqual(driver.current_url, "http://localhost:8081/")

    def testDeletePost(self):
        driver = self.driver
        self.addPost("max27@mail.ru", "12345678", "пост для удаления")
        driver.find_element_by_xpath(
            "//*[@id=\"app\"]/div/div/main/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/button/span"
        ).click()
        time.sleep(2)
        self.assertEqual(driver.current_url, "http://localhost:8081/")

    def testAddComment(self):
        driver = self.driver
        self.addPost("max27@mail.ru", "12345678", "пост для комментирования")
        driver.find_element_by_id("commentInput").send_keys("Комментарий")
        driver.find_element_by_xpath(
            "//*[@id=\"app\"]/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/div[2]/button"
        ).click()
        time.sleep(4)
        textItem = driver.find_element_by_xpath(
            "//*[@id=\"app\"]/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/v-list-tile/v-list-tile-content/div[2]"
        ).text
        time.sleep(2)
        self.assertEqual(textItem, "Комментарий")
        self.assertEqual(driver.current_url, "http://localhost:8081/")

