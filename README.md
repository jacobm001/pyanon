# pyanon

PyAnon is intended to simplify the exporting of anonimized data from any dataset.

## Why?

It often makes sense to share data for purposes of replication, collaboration, or instruction. Unfortunately, data security often prevents that from happening as readily as one might prefer. This library will hopefully facilitate these needs in as simple and transparent of a way as possible.

## An Early Example

Generally speaking, a unique identifier (uuid) is needed to associate rows. That uuid, however, could be something sensitive like a student ID number, or a social security number. The example below replaces the student id number with a newly generated uuid, which will then be saved for the entire export process.

```python
anonymizer = Anon()
cur.execute('select id, test_score from student_exams')

with open('export.csv', 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	for row in cur:
		csvwriter.write([
			anonymizer(row['id'])
			, test_score
		])
```
