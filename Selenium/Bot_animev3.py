from wsgiref.util import request_uri
from selenium import webdriver
import time 
import subprocess


PATH = "E:/Python3/Python/bot/Selenium/chromedriver.exe"

driver = webdriver.Chrome(PATH)

url = "https://www.gogoanime.co.in/videos/one-piece-episode-"

def find_elem(xpath):
    while True:
        try:
            return driver.find_element_by_xpath(xpath)
        except:
            pass
        time.sleep(0.1)
        
def dl(s):
    i, m, h= s[15:-1].split(",")
    return f"https://sbplay2.com/dl?op=download_orig&id={i[1:-1]}&mode={m[1:-1]}&hash={h[1:-1]}"

def onepiece(episode):
    driver.get(f"{url}{episode}")
    iframe = find_elem('//*[@id="root"]/div/div/div[4]/div/div[2]/div/div/div/div[2]/iframe')
    src = iframe.get_attribute("src")
    src = src.split("?")[1]
    driver.get("https://gogoplay.io/download?"+src)
    find_elem('//*[@id="content-download"]/div[2]/div[1]/a').click()
    time.sleep(3)
    for windows in driver.window_handles:
        driver.switch_to.window(windows)
        try:
            try:
                lien_dl = find_elem('/html/body/div[3]/div/table/tbody/tr[3]/td[1]/a')
            except:
                lien_dl = find_elem('/html/body/div[3]/div/table/tbody/tr[2]/td[1]/a')
            break
        except:
            driver.close()
            
    download = dl(lien_dl.get_attribute("onclick"))
    driver.get(download)
    find_elem('//*[@id="F1"]/button').click()
    lien = find_elem('//*[@id="container"]/div/span/a').get_attribute("href")

    subprocess.Popen(f"python E:/Python3/Python/bot/Selenium/dl.py {episode} {lien}")

ep_start = 953
nbr_ep = 2
for i in range(ep_start,ep_start+nbr_ep):
    onepiece(i)

driver.quit()