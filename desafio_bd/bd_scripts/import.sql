
USE testbd;

LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/Relatorio_cadop.csv'
INTO TABLE registro_operadoras
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/1T2023.csv'
INTO TABLE despesas
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/2T2023.csv'
INTO TABLE despesas
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;



LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/3T2023.csv'
INTO TABLE despesas
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;



-- Unica tabela que precisou ser formatada para o fomato DATE do MySQL --
LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/4T2023.csv'
INTO TABLE despesas
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

(
    @data_string,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
)
SET data_ = STR_TO_DATE(@data_string, '%d/%m/%Y');


LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/1T2024.csv'
INTO TABLE despesas
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/2T2024.csv'
INTO TABLE despesas
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/3T2024.csv'
INTO TABLE despesas
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/4T2024.csv'
INTO TABLE despesas
CHARACTER SET utf8
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
