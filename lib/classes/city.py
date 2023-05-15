import sqlite3

class City:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def add_city(self, name, country_id, places):
        self.cursor.execute("INSERT INTO cities (name, country_id, places) VALUES (?, ?, ?)", (name, country_id, places))
        self.conn.commit()
        print(f"City '{name}' added successfully.")

    def list_cities(self, country_id=None):
        if country_id:
            self.cursor.execute("SELECT * FROM cities WHERE country_id = ?", (country_id,))
        else:
            self.cursor.execute("SELECT * FROM cities")

        cities = self.cursor.fetchall()

        if cities:
            print("Cities:")
            for city in cities:
                print(f"- {city[1]}")
        else:
            print("No cities found.")

    def close_connection(self):
        self.conn.close()
