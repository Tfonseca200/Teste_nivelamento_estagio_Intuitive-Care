/*
Query para pegar as 10 maiores despesas do último trimestre a partir do '2024-12-31'

Lógica: 
- Baseada no cálculo (valor_final - valor_inicial)
- Quanto maior o resultado do (total_despesas) , maior é a despesas da empresa
*/

SELECT 
    ro.razao_social AS operadora, 
    ro.registro_ans,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM 
    despesas d
JOIN
    registro_operadoras ro ON d.reg_ans = ro.registro_ans
WHERE
    TRIM(d.descricao) = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND DATE_SUB("2024-12-31", INTERVAL 3 MONTH )
GROUP BY 
    ro.razao_social, ro.registro_ans
ORDER BY
    total_despesas DESC
LIMIT 10;
