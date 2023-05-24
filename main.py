
import pandas as pd
from playwright.sync_api import Playwright, sync_playwright, expect
import asyncio
from IPython.display import display
async def formatacao():
    # Lê o arquivo do Excel em um DataFrame
    df = pd.read_excel("mega.xlsx")
    #remove as linhas brugadas
    df = df.drop([0, 1, 2, 3, 4])
    # Define a primeira linha como o índice da coluna
    df.columns = df.iloc[0]

    # Remove a primeira linha
    df = df.drop(df.index[0])
    #pega a frequencia de cada Coluna
    frequencia_bola1 = df['bola 1'].value_counts()
    frequencia_bola2 = df['bola 2'].value_counts()
    frequencia_bola3 = df['bola 3'].value_counts()
    frequencia_bola4 = df['bola 4'].value_counts()
    frequencia_bola5 = df['bola 5'].value_counts()
    frequencia_bola6 = df['bola 6'].value_counts()

    #Monta o jogo em formato de array
    jogo = [frequencia_bola1.index[0], frequencia_bola2.index[0], frequencia_bola3.index[0], frequencia_bola4.index[0], frequencia_bola5.index[0], frequencia_bola6.index[0]]

    # caso você queira demonstrar a frequencia de cada coluna voce pode pegar e fazer
    # index = [frequencia_bola1.iloc[0], frequencia_bola2.iloc[0]...
    #retorna o jogo
    print(f'Tendo em mente os numeros que mais repetiram na mega-sena, O jogo que tem a maior chance de cair é o: \n{jogo[0]} {jogo[1]} {jogo[2]} {jogo[3]} {jogo[4]} {jogo[5]} ')


    return
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://asloterias.com.br/download-todos-resultados-mega-sena")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download Todos resultados da Mega Sena em Excel por ordem de sorteio").click()
    download = download_info.value
    print( download.path())
    # Save downloaded file somewhere
    download.save_as("mega.xlsx")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
asyncio.run(formatacao())
