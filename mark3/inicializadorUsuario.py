from pyautogui import *        
import pyperclip
import pyscreeze
import time
import utils
from selenium import webdriver                         
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

FAILSAFE = True           


ver_documento = r'C:\Users\Usuario\Desktop\mark4\Imagens\verDocumentos.png'
utils.insistirNoClique(ver_documento, cliques=1)
time.sleep(0.4)
insistir_no_clique = utils.encontrarImagem(ver_documento)
if type(insistir_no_clique) == pyscreeze.Box:
    while True:
        utils.insistirNoClique(ver_documento, cliques=1)
        insistir_no_clique = utils.encontrarImagem(ver_documento)
        if type(insistir_no_clique) != pyscreeze.Box:
            break          
hotkey("alt", "d", interval=0.1)
time.sleep(0.5)
hotkey("ctrl", "c")
time.sleep(0.5)      
link = pyperclip.paste()
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\Usuario\AppData\Local\Google\Chrome\User Data\Profile Selenium')
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)
driver.get(link)
    
    
time.sleep(2)
press(["tab"]*3)
write("bot.contabil")
press("tab")
write("EQSeng852@")
press("enter")
time.sleep(2)
hotkey("alt", "tab", interval=0.1)
hotkey("ctrl", "w")
hotkey("alt", "tab", interval=0.1)
time.sleep(15)
