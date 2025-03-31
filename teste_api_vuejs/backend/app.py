from fastapi import FastAPI , Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


CSV_FILE = './csv/Relatorio_cadop.csv'
df = pd.read_csv(CSV_FILE, encoding="utf-8", delimiter= ';')
df.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)

@app.get("/buscar")
def buscar_operadoras(q: str = Query(..., description="Nome da busca")):
    resultados =  df[
    
    df["Nome_Fantasia"].str.contains(q, case=False, na=False) | df["Razao_Social"].str.contains(q, case=False , na=False)

    ]

    return {"Termo": q, "resultado": resultados.to_dict(orient="records") if not resultados.empty else []}