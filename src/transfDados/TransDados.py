import tabula as tb
import pandas as pd
import zipfile
import os
import re

def limpa_texto(texto):
     if isinstance (texto , str):
          texto = re.sub(r'\s+', ' ', texto)
          texto = re.sub(r'[^\w\s]', '', texto)
          texto = texto.strip()
     return texto

PDF_PATH = '../webscraping/downloadsPdf'
CSV_PATH = 'dados_entraidos.csv'
ZIP_PATH = 'Teste_{thiago}.zip'


files = os.listdir(PDF_PATH)
files_quantity = len(files)


if files_quantity == 0:
     raise Exception("no files found int the directory")

else:

    FIRST_PDF = files[1]   
    tabelas = tb.read_pdf(PDF_PATH + '/' + FIRST_PDF, pages="all", multiple_tables=True)

    print(f"Total de tabelas extraídas: {len(tabelas)}")

    df = pd.concat(tabelas, ignore_index=True) #juntar tabelas

    print("\nEstrutura do DataFrame extraído:")
    print(df.head())


    df = df.apply(lambda col: col.map(limpa_texto) if col.dtype == "object" else col)
    df.replace({'OD': 'Odontológica', 'AMB': 'Ambulatorial'}, inplace=True) #subtituição das OD e AMB
    df.replace({'N\\A': pd.NA}, inplace=True)
    df = df.dropna(axis=1, how='all')
    df.to_csv(CSV_PATH, encoding="utf-8", index=False, sep =';')# salve cvs

    with zipfile.ZipFile(ZIP_PATH, "w") as zipf:
        zipf.write(CSV_PATH)


    print(df.head())
    print("Processo finalizado com sucesso!")



        






