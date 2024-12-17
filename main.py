from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import re
from time import sleep


# ---------------------- Entrada de dados com validação ---------------------- #
def get_valid_input(prompt, validation_fn, error_message):
    while True:
        value = input(prompt)
        if validation_fn(value):
            return value
        print(error_message)


FIREFOX_PROFILE_PATH = r"C:\Users\augus\AppData\Roaming\Mozilla\Firefox\Profiles\klo6dev5.dev-edition-default"

name = get_valid_input(
    "Informe o nome da novel: ",
    lambda x: x,
    "Nome da novel não pode ser vazio.",
)


# ------------------------- Configurações do Firefox ------------------------- #
options = Options()
options.add_argument(f"--profile={FIREFOX_PROFILE_PATH}")

# ------------------------ Inicialização do WebDriver ------------------------ #
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)


def scrape_info(link):
    """Extrai informações sobre a novel e salva em 'chapters\\info'"""
    driver.get(link)
    sleep(1)
    try:
        with open("chapters/info/metadata.txt", "w", encoding="utf8") as file:
            name = driver.find_element(By.CSS_SELECTOR, '[itemprop="name"]').text
            author = driver.find_element(By.CSS_SELECTOR, '[itemprop="author"]').text
            description = driver.find_element(
                By.CSS_SELECTOR, ".content.expand-wrapper p"
            ).text
            metadata_content = f"""---
title: {name}
creator: {author}
cover-image: cover.jpg
lang: en
description: |
  {description}
...
"""
            file.write(metadata_content)

        num_chapters = driver.find_element(
            By.XPATH, "//div[@class='header-stats']//span[1]//strong"
        ).text

        # with open("chapters/info/cover.jpg", "wb") as file:
        #     cover_element = driver.find_element(
        #         By.XPATH, "//figure[@class='cover']//img"
        #     )
        #     file.write(cover_element.screenshot_as_png)

        return num_chapters
    except Exception as error:
        print(f"Erro: {error}")
        input("Resolva o problema e pressione Enter para continuar...")
        return scrape_info()


def scrape_chapter():
    """Copia o conteúdo do capítulo atual e salva em um arquivo .md"""
    sleep(0.3)
    try:
        chapter_content = driver.find_elements(
            By.CSS_SELECTOR, "#chapter-container > p"
        )
        chapter_title = driver.find_element(By.CSS_SELECTOR, ".chapter-title").text
        chapter_num = re.search(r"Chapter (\d+)", chapter_title)
        chapter_num = chapter_num.group(1) if chapter_num else "unknown"

        with open(f"chapters/{chapter_num}.md", "w", encoding="utf8") as file:
            file.write(f"# {chapter_title}\n\n")
            for paragraph in chapter_content:
                file.write(f"{paragraph.text}\n\n")

        next_button = driver.find_element(By.CSS_SELECTOR, ".nextchap")
        next_button.click()

        print(f"Capítulo {chapter_num} copiado com sucesso!")
    except Exception as error:
        print(f"Erro: {error}")
        input("Resolva o problema e pressione Enter para continuar...")
        scrape_chapter()


if __name__ == "__main__":
    # ---------------------------- Inicialização ---------------------------- #
    name_link = name.lower().replace(" ", "-")
    link = f"https://www.lightnovelpub.com/novel/{name_link}"
    num_chapters = scrape_info(link)

    # ---------------------------- Cópia dos capítulos ---------------------------- #
    start_chapter = get_valid_input(
        "Informe o capítulo inicial (ex: 1): ",
        lambda x: x.isdigit(),
        "Capítulo inicial deve ser um número inteiro.",
    )

    driver.get(f"{link}/chapter-{start_chapter}")
    for _ in range(int(num_chapters) - int(start_chapter) + 1):
        scrape_chapter()

    # ---------------------------- Finalização ---------------------------- #
    driver.quit()
    print("Capítulos copiados com sucesso!")
