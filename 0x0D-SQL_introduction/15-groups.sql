-- list the number of records with the same score in thr table second_table
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY number DESC;
