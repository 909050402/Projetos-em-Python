from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) # headless
    pagina = navegador.new_page()
    pagina.goto("https://dlivros.com/categoria/autoajuda")

    #aqui eu pego a quantidade de elementos que eu possuo naquela página
    quantidade = pagina.locator("//strong//a").count()
    #aqui eu pego o link para depois numa automação fazer o download dos livros, por exemplo
    link = pagina.locator("//strong//a")
    #aqui eu pego o nome dos livros
    elemento = pagina.locator("//strong//a")

    #aqui eu peço pra fazer o print, porém eu poderia jogar numa base de dados por exemplo
    for i in range(quantidade):
        print(elemento.nth(i).text_content())
        print(elemento.nth(i).get_attribute("href"))
        


    