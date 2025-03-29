import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import zipfile


def download_files(url, destination_folder):
    """Baixa todos os arquivos PDF da URL especificada para a pasta de destino."""
    os.makedirs(destination_folder, exist_ok=True)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = soup.select("a[href$='.pdf']")

    if not pdf_links:
        print("Nenhum PDF encontrado.")
        return

    for link in pdf_links:
        pdf_url = urljoin(url, link["href"])
        file_name = os.path.join(destination_folder, pdf_url.split("/")[-1])

        print(f"Baixando: {file_name}")
        with open(file_name, "wb") as f:
            f.write(requests.get(pdf_url).content)

    print("\nDownload dos PDFs concluído!\n")


def compress_zip(zip_destination, destination_folder):
    """Compacta todos os arquivos da pasta de destino em um arquivo ZIP."""
    items = os.listdir(destination_folder)
    files = [item for item in items if os.path.isfile(os.path.join(destination_folder, item))]

    if not files:
        print("Nenhum arquivo encontrado para compactar. O ZIP não será criado.")
        return

    with zipfile.ZipFile(zip_destination, "w") as zipf:
        for root, _, file_names in os.walk(destination_folder):
            for file_name in file_names:
                zipf.write(os.path.join(root, file_name), file_name)

    print(f"Arquivo ZIP criado: {zip_destination}")
