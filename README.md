<h2 align="center" style="font-size: 40px">Teste de nivelamento de estágio de desenvolviento de software</h2>

<br>

## Objetivo 🎯

Repositório desenvolvido para os testes técnicos de nivelamento do processo seletivo de estágio da empresa __Intuitive Care__.

O objetivo é avaliar as habilidades técnicas em quatro áreas fundamentais para a vaga de estágio em desenvolvimento:

1. **Web Scraping**  
2. **Transformação de Dados**  
3. **Testes com Banco de Dados**  
4. **Consumo/Desenvolvimento de APIs**  


## Testes do desafio de nivelamento

- Teste de WebScraping
- Teste de tranformação de dados
- Teste de banco de dados
- Teste de API


## ⚙️ Tecnologias usadas nos testes

- Python
- SQL com MSQL
- Docker
- Docker-compose
- FastAPI
- Vue js
- Git - Utilização de duas branchs (dev,main)
- Git LFS (Para otimização dos arquivos grandes CSVs)


<br>

## ℹ️ Justificativas da escolha da linguagem

Os primeiros dois testes de nivelamento me dá opção de usar Java ou Python para a realização das tasks!

Por mais que eu tenha mais familiaridade com a sixtaxe da linguagem java , optei por utilizar Python para a realização dos desafios, pois como tem um foco em extração e manipulação de arquivos, Python tem bibliotecas muito versáteis e flexíveis para esse foco.


<br>

## Pré-requisitos
- Python 3+: versão do python compatível 3.13.2 ou mais.
- pip: Gerenciador de pacotes do Python.
- Git: Versionamento de codígo.

<br>

## ⚙ Passo a passo pra inicia os testes e downloads de libs

Clone o repósitorio e entre nele:

```bash
git clone https://github.com/Tfonseca200/Teste_nivelamento_estagio_Intuitive-Care.git
cd Teste_nivelamento_estagio_Intuitive-Care
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- No windows

```bash
.\venv\Scripts\activate
```
- No Linux/MacOS:

```bash
source venv/bin/activate
```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Dependencias do projeto intalados!

<br>

## 📋 Estrutura do Projeto  
```plaintext
├── web_scraping/       # Códigos e download de PDFs e compactação para ZIP
├── trans_dados/        # Extração de dados de PDF , estrutura de dados em CSVs compactação para ZIP
├── teste_bd/           # Scripts para importação de dados de CSVs para banco de dados
├── teste_api_vuejs/    # Códigos para consumir/criar APIs
└── README.md           # Documentação principal do repositorio
```

# Navegação entre READMES de cada testes

| README | Descrição |
| --- | ------- |
| [README Web Scraping](/webscraping/README.md) | Documentação do teste Web Scraping |
| [README Tranformação de dados](/transf_dados/README.md) | Documentação do teste de transformação de dados|
| [README Banco de dados](/teste_bd/README.md) | Documentação do teste de banco da dedos |
| [README API](/teste_api_vuejs/README.md) | Documentação do teste de API e interface VUE js |
<br>

## 🛜 Referências e fontes de informação

W3 schools (python, SQL): https://www.w3schools.com<br>
FastAPI do Zero: https://fastapidozero.dunossauro.com<br>
Iniciando com vue.js do zero:  https://medium.com/@thais.ribeiro/iniciando-com-vue-js-criando-um-projeto-do-zero-b62e159ca1a7<br>
IA LLM: Para revisão de conceitos e pesquisas de libs

<br>

## 👨🏻‍💻 Autor

### Thiago Fonseca Claudino

<p>
  <img src="asserts/IMG_20240223_083843_145.jpg" alt="imagem do autor" width="150">
</p>


<div align="left">
  <a href="https://www.linkedin.com/in/thiago-fonseca-tech" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="linkedin logo"  />
  </a>
</div>
