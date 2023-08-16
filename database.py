import mysql.connector
from datetime import datetime


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='evidentbdtest'
        )
        self.cursor = self.conn.cursor()

    def create_user(self, name, email, password):
        query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (name, email, password))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_user_by_email(self, email):
        query = "SELECT user_id, name, email, password FROM users WHERE email = %s"
        self.cursor.execute(query, (email,))
        return self.cursor.fetchone()

    def store_comma_integers(self, user_id, input_value):
        query = "INSERT INTO khoj (user_id, input_value, time_stamp) VALUES (%s, %s, %s)"
        timestamp = datetime.now()
        self.cursor.execute(query, (user_id, input_value, timestamp))
        self.conn.commit()

    def get_input_values_by_time_range(self, start_datetime, end_datetime, user_id):
        query = """
            SELECT timestamp, input_value
            FROM khoj
            WHERE user_id = %s AND time_stamp BETWEEN %s AND %s
        """
        self.cursor.execute(query, (user_id, start_datetime, end_datetime))
        results = self.cursor.fetchall()

        input_values_data = []
        for row in results:
            timestamp, input_value = row
            input_values_data.append({
                "timestamp": timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                "input_values": input_value
            })

        return input_values_data
