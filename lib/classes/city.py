import sqlite3

class City:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def add_city(self, name, country_id):
        self.cursor.execute("INSERT INTO cities (name, country_id) VALUES (?, ?, ?)", (name, country_id))
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

    def search_cities(self, search_term):
        self.cursor.execute("SELECT * FROM cities WHERE name LIKE ?", ('%' + search_term + '%',))
        cities = self.cursor.fetchall()

        if cities:
            print("Search results:")
            for city in cities:
                print(f"- {city[1]} (Country ID: {city[2]})")
        else:
            print("No cities found.")