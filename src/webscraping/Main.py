from WebScraping import baixarArquivos,compactarEmZip

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
PASTA_DESTINO = "downloadsPdf"
ZIP_DESTINO = "anexos.zip"

if __name__ == "__main__":
    baixarArquivos(URL, PASTA_DESTINO)
    compactarEmZip(ZIP_DESTINO, PASTA_DESTINO)