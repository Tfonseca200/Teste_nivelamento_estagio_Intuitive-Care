import tabula as tb
import pandas as pd
import zipfile
import os


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
    df = pd.concat(tabelas, ignore_index=False) # juntar tableas
    df.replace({'OD': 'Odontológica', 'AMB': 'Ambulatorial'}, inplace=True) #subtituição das OD e AMB
    df.to_csv(CSV_PATH, encoding="utf-8", index=False) # salve cvs
    with zipfile.ZipFile(ZIP_PATH, "w") as zipf:
         zipf.write(CSV_PATH)

    print("Processo finalizado com sucesso!")
        






