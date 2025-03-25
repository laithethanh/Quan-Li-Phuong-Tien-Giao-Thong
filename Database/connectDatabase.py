import mysql.connector
from mysql.connector import Error


class ConnectDatabase:
    def __init__(self):
        self.host = "localhost"
        self.database = "qlx"
        self.user = "root"
        self.password = ""

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
            )
            if connection.is_connected():
                print("ket noi thanh cong")
                return connection
        except Error as e:
            print("loi ket noi:", e)