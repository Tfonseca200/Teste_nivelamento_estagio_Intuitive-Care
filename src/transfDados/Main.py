

from TransDados import clear_texto , extract_data_from_pdf, compress_csv_in_zip


PDF_PATH = '../webscraping/downloadsPdf'
CSV_PATH = 'dados_entraidos.csv'
ZIP_PATH = 'Teste_{thiago}.zip'


if __name__ == "__main__":

    extract_data_from_pdf(PDF_PATH , CSV_PATH)
    compress_csv_in_zip(CSV_PATH, ZIP_PATH)