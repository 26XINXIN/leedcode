SELECT Scores.Score, CAST(ROWNUM AS SIGNED) as Rank
FROM Scores LEFT JOIN ((
    SELECT t1.Score, (@row := @row + 1) AS ROWNUM
    FROM (SELECT DISTINCT Score from Scores ORDER BY Score DESC) AS t1,
    (SELECT (@row := 0)) AS t2
) AS Ranks) ON Scores.Score=Ranks.Score
ORDER BY Score DESC;
