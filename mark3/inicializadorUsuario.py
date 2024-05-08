import pyautogui        
import pyperclip
import time
from selenium import webdriver                         
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

pyautogui.FAILSAFE = True           


def encontrar_imagem(imagem):
    while True:
        try:
            encontrou = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.8)
            return encontrou
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            print("Imagem não encontrada.")
            pass

clicar = encontrar_imagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\microsiga.png')
pyautogui.click(clicar)
time.sleep(0.5)
clicar2 = encontrar_imagem(r'C:\Users\User\OneDrive - EQS Engenharia Ltda\Documentos\GitHub\GitHubDoJessezinho\mark3\Imagens\verDocumentos.png')
time.sleep(0.5)
pyautogui.click(clicar2, clicks=2)
time.sleep(1)        
pyautogui.hotkey("alt", "d", interval=0.04)  
pyautogui.hotkey("ctrl", "c")
link = pyperclip.paste()
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data\Perfil Selenium')
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)
driver.get(link)
time.sleep(2)
pyautogui.press(["tab"]*3)
pyautogui.write("jesse.silva")
pyautogui.press("tab")
pyautogui.write("Neo@7592")
pyautogui.press("enter")
time.sleep(30)


