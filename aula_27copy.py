#importacao padrao
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager # abrir

import time

email_fic = "pythonautomacaoctrlplay@gmail.com"
senha_fic = "ctrlplay"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 

driver.get("https://accounts.google.com/") 
time.sleep(5)

email_input = driver.find_element(By.ID,'identifierId')
email_input.send_keys(email_fic)
email_input.send_keys(Keys.RETURN)
time.sleep(5)

senha_input = driver.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input")
senha_input.send_keys(senha_fic)
senha_input.send_keys(Keys.RETURN)
time.sleep(5)

driver.get("https://youtube.com.br")
time.sleep(5)

Barra_de_pesquisa = driver.find_element(By.NAME,'search_query')
Barra_de_pesquisa.clear()
Barra_de_pesquisa.send_keys("videos de matematica para vestibular")
Barra_de_pesquisa.send_keys(Keys.RETURN)
time.sleep(5)

cont = 0
videos = driver.find_elements(By.XPATH, '//a[@id="video-title"]')

for i in range(len(videos)):

    video = videos[i].get_attribute("href")

    if "shorts" not in video:
        videos[cont] = video
        cont+=1

videos = videos[:cont]

cont_video = 0
for video in videos:
    driver.get(video)
    time.sleep(5)
    driver.get(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button/yt-touch-feedback-shape/div/div[2]')
    time.sleep(3)
    cont_video+=1
    print(cont_video)




