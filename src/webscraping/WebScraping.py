import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import zipfile


def baixarArquivos(URL, PASTA_DESTINO):
    os.makedirs(PASTA_DESTINO, exist_ok=True)
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    pdfLinks = soup.select("a[href$='.pdf']")

    if not pdfLinks:
        print("PDF não encontrado")
        return

    for link in pdfLinks:
        pdfUrl = urljoin(URL, link["href"])
        fileName = os.path.join(PASTA_DESTINO, pdfUrl.split("/")[-1])

        print(f"Baixando: {fileName}")
        with open(fileName, "wb") as f:
            f.write(requests.get(pdfUrl).content)

    print("\n Download dos PDFs concluído!\n")


def compactarEmZip(ZIP_DESTINO , PASTA_DESTINO):

    itens = os.listdir(PASTA_DESTINO)
    arquivos = []

    for item in itens:
        caminhoCompleto = os.path.join(PASTA_DESTINO, item) #Caminho completo
        if os.path.isfile(caminhoCompleto): #Verifica se é um item
            arquivos.append(item)

    if not arquivos:
        print("Nenhum arquivo encontrado para compactar. O ZIP não será criado.")
    
    else:
        with zipfile.ZipFile(ZIP_DESTINO, "w") as zipf:
            for root, _, files in os.walk(PASTA_DESTINO):
                for file in files:
                    zipf.write(os.path.join(root, file), file)
            print(f"Arquivo ZIP criado: {ZIP_DESTINO}")

