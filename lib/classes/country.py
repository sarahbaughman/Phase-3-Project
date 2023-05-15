import sqlite3

class Country:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def add_country(self, name):
        self.cursor.execute("INSERT INTO countries (name) VALUES (?)", (name,))
        self.conn.commit()
        print(f"Country '{name}' added successfully.")

    def list_countries(self):
        self.cursor.execute("SELECT * FROM countries")
        countries = self.cursor.fetchall()

        if countries:
            print("Countries:")
            for country in countries:
                print(f"- {country[1]}")
        else:
            print("No countries found.")

    def close_connection(self):
        self.conn.close()

    def search_countries(self, search_term):
        self.cursor.execute("SELECT * FROM countries WHERE name LIKE ?", ('%' + search_term + '%',))
        countries = self.cursor.fetchall()

        if countries:
            print("Search results:")
            for country in countries:
                print(f"- {country[1]}")
        else:
            print("No countries found.")