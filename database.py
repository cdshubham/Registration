import mysql.connector

db_config = {
        'user': 'root',
        'password': 'mysql',
        'host': 'localhost',
    }

    # Establish a connection to the database
conn = mysql.connector.connect(**db_config)

    # Create a cursor object to execute SQL queries
cursor = conn.cursor()

def dbms_enter(data):
    

    cursor.execute("create database if not exists registration");
    cursor.execute("use registration");
    print("Hello");
    # Data to insert


    cursor.execute("""Create table if not exists users(
                name varchar(20),
                university_no varchar(10) primary key,
                email varchar(30),
                age int,
                phone_no varchar(10)
    )""")

    # SQL query to insert data
    insert_query = "INSERT INTO users (name,university_no, email, age,phone_no) VALUES (%s, %s, %s, %s, %s)";
    cursor.execute(insert_query, (data['name'], data['university_no'], data['email'], data['age'], data['phone_no']))


    # Commit the changes to the database
    conn.commit()

    print("Data inserted successfully!")


def dbms_out(data):

    cursor.execute("use registration");
    print("Hello");


    # Execute a SELECT query
    query = f"SELECT * FROM users where university_no={data}"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchone()

    # Print the rows
    print(rows)

    return rows


def dbms_update(data,Id):


    cursor.execute("use registration");
    print("Hello");
    update_query = "UPDATE users SET "
    update_values = []
    for column, value in data.items():
        update_query += f"{column} = %s, "
        update_values.append(value)
    update_query = update_query.rstrip(", ") + " WHERE university_no = %s"
    update_values.append(Id)
    
    cursor.execute(update_query, update_values)
    
    # Commit the changes
    conn.commit()