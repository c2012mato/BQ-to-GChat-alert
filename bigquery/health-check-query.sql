-- Example: Nulls check for a required column
SELECT
  COUNT(*) AS null_count
FROM `your_project.your_dataset.your_table`
WHERE required_col IS NULL
