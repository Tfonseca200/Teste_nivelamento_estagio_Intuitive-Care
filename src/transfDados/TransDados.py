import tabula as tb
import pandas as pd
import zipfile
import os


PDF_PATH = "../webscraping/downloadsPdf/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
CSV_PATH = "dados_entraidos.csv"
ZIP_PATH = "Teste_{thiago}.zip"


tabelas = tb.read_pdf(PDF_PATH, pages="all", multiple_tables=True)

df = pd.concat(tabelas, ignore_index=True) # juntar tableas

df.replace({'OD': 'Odontológica', 'AMB': 'Ambulatorial'}, inplace=True) #subtituição das OD e AMB


df.to_csv(CSV_PATH, encoding="utf-8", index=False) # salve cvs

with zipfile.ZipFile(ZIP_PATH, "w") as zipf:
    zipf.write(CSV_PATH)

print("Processo finalizado com sucesso!")




