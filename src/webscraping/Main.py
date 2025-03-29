from WebScraping import download_files,compress_zip

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
DESTINATION_FILE = "downloadsPdf"
ZIP_DESTINATION = "anexos.zip"

if __name__ == "__main__":
    download_files(URL, DESTINATION_FILE)
    compress_zip(ZIP_DESTINATION, DESTINATION_FILE)