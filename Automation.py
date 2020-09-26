from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import font
import tkinter as tk
import time 

import time
HEIGHT = 720
WIDTH= 720
root = tk.Tk()

def signUp(username, password, crns):
    PATH = "/Users/matthewennis/PycharmProjects/ClassAutomation/chromedriver"
    driver = webdriver.Chrome(PATH)

    driver.get("https://myuvm.uvm.edu/web/home-community/registrar")

    UsernameField = driver.find_element_by_name("username")
    UsernameField.send_keys(username)

    PasswordField = driver.find_element_by_name("password")
    PasswordField.send_keys(password)
    PasswordField.send_keys(Keys.RETURN)

    try:
        AddDropWithdraw = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "ADD/DROP/WITHDRAW"))
        )
        AddDropWithdraw.click()
    except:
        driver.quit()

    driver.switch_to.frame("bannerFrame")
    try:
        TermSubmit = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "term_in"))
        )
        TermSubmit.submit()
    except:
        driver.quit()

    for x in range(len(crns)):
        try:
            CRNField = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "crn_id"+str(x+1)))
            )
            CRNField.send_keys(crns[x])
        except:
            driver.quit()

    SubmitCRNS= driver.find_element_by_xpath("html/body/div[3]/form/input[20]")
    SubmitCRNS.click()


canvas= tk.Canvas(root, height= HEIGHT, width= WIDTH)
canvas.pack()

backgroundImage = tk.PhotoImage(file="catamount1.png")
backgroundLabel= tk.Label(root, image=backgroundImage)
backgroundLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

topFrame = tk.Frame(root, bg = "#007155")
topFrame.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.05)

title = tk.Label(topFrame, text= "UVM Class Sign Up", font=('Courier', 20), bg ="#FFD416")
title.pack(fill='both')


usernameLabel = tk.Label(topFrame, text= "NetID:", font=('Courier', 15), bg ="#FFD416")
usernameLabel.place(relx=0.1, rely=0.25, relwidth=0.35, relheight=0.2)
usernameEntry=tk.Entry(topFrame)
usernameEntry.place(relx=0.1, rely=0.5, relwidth=0.35, relheight=0.2)

passwordLabel = tk.Label(topFrame, text= "Password:", font=('Courier', 15), bg ="#FFD416")
passwordLabel.place(relx=0.6, rely=0.25, relwidth=0.35, relheight=0.2)
passwordEntry=tk.Entry(topFrame)
passwordEntry.config(show="*")
passwordEntry.place(relx=0.6, rely=0.5, relwidth=0.35, relheight=0.2)

bottomFrame = tk.Frame(root, bg = "#007155")
bottomFrame.place(relwidth=0.9, relheight=0.25, relx=0.05, rely=0.7)

passwordLabel = tk.Label(bottomFrame, text= "CRNS:", font=('Courier', 15), bg ="#FFD416")
passwordLabel.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.2)
d={}
for i in range(1,9):
    d["crn{0}".format(i)]=tk.Entry(bottomFrame)
    d["crn"+str(i)].place(relx=0.12*(i)-0.08, rely=0.4, relwidth=0.1, relheight=0.2)


goButton = tk.Button(bottomFrame, text="Go", command=lambda: signUp(usernameEntry.get(),passwordEntry.get(),[d["crn1"].get(),d["crn2"].get(),d["crn3"].get(),d["crn4"].get(),d["crn5"].get(),d["crn6"].get(),d["crn7"].get(),d["crn8"].get()]))
goButton.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.2)

root.mainloop()

