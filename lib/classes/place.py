import sqlite3

class Place:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def add_place(self, name, type, city_id):
        self.cursor.execute("INSERT INTO places (name, city_id) VALUES (?, ?)", (name, type, city_id))
        self.conn.commit()
        print(f"Place '{name}' added successfully.")

    def list_places(self, city_id=None):
        if city_id:
            self.cursor.execute("SELECT * FROM places WHERE city_id = ?", (city_id,))
        else:
            self.cursor.execute("SELECT * FROM places")

        places = self.cursor.fetchall()

        if places:
            print("Places:")
            for place in places:
                print(f"- {place[1]}")
        else:
            print("No places found.")

    def close_connection(self):
        self.conn.close()

    def search_places(self, search_term):
        self.cursor.execute("SELECT * FROM places WHERE name LIKE ?", ('%' + search_term + '%',))
        places = self.cursor.fetchall()

        if places:
            print("Search results:")
            for place in places:
                print(f"- {place[1]} (City ID: {place[2]})")
        else:
            print("No places found.")