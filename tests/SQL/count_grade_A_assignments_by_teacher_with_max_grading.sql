-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT
  COUNT(CASE WHEN a.grade = 'A' THEN 1 END) AS grade_a_count
FROM
  teachers t
JOIN
  assignments a ON t.id = a.teacher_id
WHERE
  a.state = 'GRADED'
GROUP BY
  t.id
ORDER BY
  COUNT(a.id) DESC
LIMIT 1;
