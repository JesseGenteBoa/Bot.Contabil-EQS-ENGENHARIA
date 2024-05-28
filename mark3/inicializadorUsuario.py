from pyautogui import *        
import pyperclip
import time
import utils
from selenium import webdriver                         
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

FAILSAFE = True           


while True:
    try:
        botao = r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\verDocumentos.png'
        utils.insistirNoClique(botao)          
        hotkey("alt", "d", interval=0.1)
        time.sleep(0.5)
        hotkey("ctrl", "c")
        time.sleep(0.5)      
        link = pyperclip.paste()
        options = webdriver.ChromeOptions()
        options.add_argument(r'user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data\Perfil Selenium')
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico, options=options)
        driver.get(link)
        break
    except:
        time.sleep(0.3)
        hotkey("alt", "tab", interval=0.1)
        hotkey("ctrl", "w")
        time.sleep(0.2)
        driver.quit
    
time.sleep(2)
press(["tab"]*3)
write("bot.contabil")
press("tab")
write("EQSeng852@")
press("enter")
time.sleep(30)
