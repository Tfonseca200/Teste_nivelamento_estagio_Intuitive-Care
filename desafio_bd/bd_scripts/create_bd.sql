CREATE TABLE IF NOT EXISTS registro_operadoras (
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(20) NOT NULL UNIQUE,
    razao_social VARCHAR(120),
    nome_fantasia VARCHAR(120),
    modalidade VARCHAR(120),
    logradouro VARCHAR(120),
    numero VARCHAR(20),
    complemento VARCHAR(30),
    bairro VARCHAR(30),
    cidade VARCHAR(30),
    uf VARCHAR(2),
    cep VARCHAR(20),
    ddd VARCHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    enderenco_eletronico VARCHAR(50),
    representante VARCHAR(30),
    cargo_representante VARCHAR(30),
    regiao_comercializacao VARCHAR(10),
    data_registro_ans VARCHAR(10)
)CHARACTER SET utf8 COLLATE utf8_general_ci;


CREATE TABLE IF NOT EXISTS despesas(
    data_ DATE,
    reg_ans INT,
    cd_conta_contabil VARCHAR(20),
    descricao VARCHAR(200),
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL
)CHARACTER SET utf8 COLLATE utf8_general_ci;