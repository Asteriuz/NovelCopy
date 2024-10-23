from typing import Container
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import re
from time import sleep

link = "https://www.lightnovelpub.com/novel/shadow-slave-1365"
start_chapter = "1428"
number_of_chapters = 1000


DATA_DIR = r"C:\Users\augus\AppData\Local\Google\Chrome\User Data"
CHROMEDRIVER_PATH = r"C:\Users\augus\.wdm\drivers\chromedriver\win64\127.0.6533.88\chromedriver-win32\chromedriver.exe"

options = Options()
options.add_argument(f"user-data-dir={DATA_DIR}")

driver = webdriver.Chrome(
    service=Service(CHROMEDRIVER_PATH), options=options
)


driver.get(f"{link}/chapter-{start_chapter}")


def create():
    sleep(0.3)
    try:
        chapter_container = driver.find_elements(
            By.CSS_SELECTOR, "#chapter-container > p"
        )
        chapter_title = driver.find_element(By.CSS_SELECTOR, ".chapter-title").text
        chapter_num = re.search(r"Chapter (\d+)", chapter_title)
        if chapter_num:
            chapter_num = chapter_num.group(1)

        with open(f"chapters/{chapter_num}.md", "w", encoding="utf8") as file:
            file.write(f"# {chapter_title}\n\n")
            for p in chapter_container:
                file.write(f"{p.text}\n\n")

        next = driver.find_element(By.CSS_SELECTOR, ".nextchap")
        next.click()

        print(f"{chapter_num} copiado com sucesso!")
    except Exception as e:
        input("Resolva a verificação e pressione enter para continuar...")
        create()


i = 0
while i < int(number_of_chapters):
    create()
    i += 1
sleep(500)

print("Capítulos copiados com sucesso!!")
