import sqlite3
import pandas as pd
import os
# TO IMPORT THE DB, JUST UN-COMMENT THE SECTION NEEDED

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
# print("CONNECTION:", connection) - Debug confirmation

cursor = connection.cursor()
# print("CURSOR", cursor) - Debug Confirmation


### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!
### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!
### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!
### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!
### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!
### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!

# df = pd.read_csv('buddymove_holidayiq.csv')


# the_stuff = df.to_sql(name='review', con=connection)

# cursor.execute(the_stuff)
# connection.commit
# connection.close

### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!
### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!
### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!
### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!
### IMPORTING THE DF HAS BEEN COMMENTED OUT. THIS SHOULD ONLY BE DONE ONCE!!

# How many rows?

row_count = 'SELECT COUNT(*) FROM review'

rows = cursor.execute(row_count).fetchall()

print("How many rows?", rows)

# How many users reviewed at least 100 nature and 100 shopping?

reviewers = 'SELECT COUNT(*) FROM review WHERE review.Nature > 100 AND review.Shopping > 100'

reviewers_answer = cursor.execute(reviewers).fetchall()

print('How many users reviewed at least 100 Nature and 100 Shopping?', reviewers_answer)

# What are the average number of reviews for each category?

averages = 'SELECT AVG(review.Sports), AVG(review.Religious), AVG(review.Nature), AVG(review.Theatre), AVG(review.Shopping), AVG(review.Picnic) FROM review'

avgs_answer = cursor.execute(averages).fetchall()

print("Average reviews per category", avgs_answer)