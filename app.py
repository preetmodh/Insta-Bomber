from flask import Flask,request,render_template
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
#to add selenium on heroku
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get("http://www.instagram.com")
sleeep(10)
# Now you can start using Selenium
app = Flask(__name__, template_folder='template')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/do",methods=["POST"])
def do():
    User_Name=request.form.get("username")
    Pass_Word=request.form.get("password")
    Messages=request.form.get("message")
    n=request.form.get("number")
    TO_Whom=request.form.get("username2")
    driver.get("http://www.instagram.com")
    
    
    sleep(2)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys(User_Name)   
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(Pass_Word)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(8)
    
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
    sleep(3)
    
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    sleep(5)
    
    driver.get("https://www.instagram.com/"+TO_Whom+"/")
    sleep(5)
    driver.find_element_by_xpath('//button[@type="button"]').click()
    sleep(3)
    print('MESSAGING!!')
    for j in range(int(n)):
        driver.find_element_by_xpath('//textarea[@placeholder="Message..."]').send_keys(Messages,Keys.ENTER)
        sleep(2)
    return "DONE!!!!"
