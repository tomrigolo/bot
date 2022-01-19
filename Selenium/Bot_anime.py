from wsgiref.util import request_uri
from selenium import webdriver
import time 
import subprocess



PATH = "chromedriver.exe"

driver = webdriver.Chrome(PATH)

url = "https://www.gogoanime.co.in/videos/one-piece-episode-"

def dl(s):
    i, m, h= s[15:-1].split(",")
    return f"https://sbplay2.com/dl?op=download_orig&id={i[1:-1]}&mode={m[1:-1]}&hash={h[1:-1]}"

def onepiece(episode):
    driver.get(f"{url}{episode}")
    time.sleep(5)
    iframe = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[2]/div/div/div/div[2]/iframe')
    src = iframe.get_attribute("src")
    src = src.split("?")[1]
    driver.get("https://gogoplay.io/download?"+src)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="content-download"]/div[2]/div[1]/a').click()
    time.sleep(5)

    print(driver.window_handles)
    for windows in driver.window_handles:
        driver.switch_to.window(windows)
        try:
            try:
                lien_dl = driver.find_element_by_xpath('/html/body/div[3]/div/table/tbody/tr[3]/td[1]/a')
            except:
                lien_dl = driver.find_element_by_xpath('/html/body/div[3]/div/table/tbody/tr[2]/td[1]/a')
            break
        except:
            pass
            
    download = dl(lien_dl.get_attribute("onclick"))
    driver.get(download)
    time.sleep(12)
    driver.find_element_by_xpath('//*[@id="F1"]/button').click()
    time.sleep(5)
    lien = driver.find_element_by_xpath('//*[@id="container"]/div/span/a').get_attribute("href")
    
    subprocess.Popen(f"python E:/Python3/Python/bot/Selenium/dl.pydl.py {episode} {lien}")
    
for i in range(890,895):
    onepiece(i)

