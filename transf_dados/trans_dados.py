import tabula as tb
import pandas as pd
import zipfile
import os
import re

def clear_texto(texto):
     if isinstance (texto , str):
          texto = re.sub(r'\s+', ' ', texto)
          texto = re.sub(r'[^\w\s]', '', texto)
          texto = texto.strip()
     return texto



#função para extrair dados do PDF
def extract_data_from_pdf(PDF_PATH, CSV_PATH):
    files = os.listdir(PDF_PATH)
    files_quantity = len(files)


    if files_quantity == 0:
         raise Exception("no files found int the directory")

    else:

        FIRST_PDF = files[1]
        tabelas = tb.read_pdf(PDF_PATH + '/' + FIRST_PDF, pages="all", multiple_tables=True, lattice=True, stream=True)
        df = pd.concat(tabelas, ignore_index=True) #juntar tabelas

        df.replace({'N\\A': pd.NA}, inplace=True)
        df = df.apply(lambda col: col.map(clear_texto) if col.dtype == "object" else col)
        df = df.dropna(axis=1, how='all')
        df.replace({'OD': 'ODONTOLÓGICA', 'AMB': 'AMBULATORIAL'}, inplace=True)  # subtituição das OD e AMB
        df.to_csv(CSV_PATH, encoding="utf-8", index=False, sep =';')# salve cvs


        print("Dados de PDF extraindo para tabela estruturada em csv\n")
        print(df.head())



#função para compactar csv em zip
def compress_csv_in_zip(CSV_PATH, ZIP_PATH):
    with zipfile.ZipFile(ZIP_PATH, "w") as zipf:
        zipf.write(CSV_PATH)

    print(f"Arquivo zip criado: {ZIP_PATH}")



        






