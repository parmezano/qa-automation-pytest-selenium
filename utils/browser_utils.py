class BrowserUtils:

    def __init__(self, driver):
        self.driver = driver


    def getTitle(self):
        return self.driver.title


    def getCurrentUrl(self):
        return self.driver.current_url


    def scrollToBottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def refreshPage(self):
        self.driver.refresh()
