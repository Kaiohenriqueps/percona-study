import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="kaio",
    password="changethispassword",
    database="mydb",
    cursorclass=pymysql.cursors.DictCursor,
)

batches = [(f"webmaster{i}@python.org", f"very-secret-{i}") for i in range(1, 1000)]

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.executemany(sql, batches)
    connection.commit()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    connection.close()
