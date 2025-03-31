
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
    AND DATE_SUB("2024-12-31", INTERVAL 3 MONTH)
GROUP BY 
    ro.razao_social, ro.registro_ans
ORDER BY
    total_despesas DESC
LIMIT 10;

