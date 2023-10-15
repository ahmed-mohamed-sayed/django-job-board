/* Formatted on 2/23/2023 6:43:23 AM (QP5 v5.294) */
SELECT TO_CHAR(creation_date, 'yyyy-mm-dd'), COUNT (*)
  FROM UBA.CUSTOMER
 WHERE CREATION_DATE --BETWEEN TRUNC (SYSDATE - 1) AND TRUNC (SYSDATE) 
 between  TO_DATE ('01/01/2023 00:00:00','dd/mm/yyyy hh24:mi:ss') AND TO_DATE ('01/02/2023 23:59:59','dd/mm/yyyy hh24:mi:ss')
       AND CUSTOMERREGISTRATIONTYPE = 5
 GROUP BY TO_CHAR(creation_date, 'yyyy-mm-dd') 
 ORDER BY 1 ;