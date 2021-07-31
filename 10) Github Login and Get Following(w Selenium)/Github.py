from GithubUserInfo import username,password
from selenium import webdriver
import time

class Github:
    def __init__(self,username,password): 
        self.driver=webdriver.Chrome()
        self.username=username
        self.password=password
        self.following=[]

    def signIn(self):
        self.driver.get("https://github.com/login") 
        time.sleep(2)   
        
        username=self.driver.find_element_by_xpath("//*[@id='login_field']")
        password=self.driver.find_element_by_xpath("//*[@id='password']")

        username.send_keys(self.username)
        password.send_keys(self.password)

        time.sleep(1)

        button=self.driver.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]")
        button.click()

    def getFollowing(self):
        self.driver.get(f"https://github.com/{self.username}?tab=following")
        time.sleep(2)
        items=self.driver.find_elements_by_css_selector(".d-table.table-fixed")
        for item in items:
            newItem=item.find_element_by_css_selector(".f4.Link--primary").text#class attribute ı iki adet isme sahipti o yüzden iki adet . koyduk
            self.following.append(newItem)



github=Github(username,password)
github.signIn()
github.getFollowing()



