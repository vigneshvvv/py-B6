from dbConnection import get_connection, closeConnection

def fetch_studentDetails():
    connection = get_connection()

    if connection is None:
        print("Failed to Establish connection")
        return

    cursor = connection.cursor(dictionary=True)
    query = "select * from students"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    closeConnection(connection, cursor)

def fetchUserById(id, name):
    connection = get_connection()

    if connection is None:
        print("Failed to Establish connection")
        return

    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from students where student_id = %s and student_name = %s", (id, name))
    data = cursor.fetchone()
    print(data)
    closeConnection(connection, cursor)

def insertData(data):
    connection = get_connection()
    if connection is None:
        print("Failed to Establish connection")
        return

    cursor = connection.cursor()
    query = "INSERT into students VALUES (%s, %s, %s)"
    values = (data["student_id"], data["student_name"], data["department"])
    cursor.execute(query, values)
    connection.commit()
    print("Inserted data")
    closeConnection(connection, cursor)

# fetch_studentDetails()
# fetchUserById(2, "Arun")

insertData({
    "student_id": 9,
    "student_name": "Raju",
    "department": "DEV"
})

