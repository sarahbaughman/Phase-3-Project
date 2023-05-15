import sqlite3

def create_tables():
    conn = sqlite3.connect('./classes/database.db')
    cursor = conn.cursor()

    # Create the countries table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create the cities table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            country_id INTEGER NOT NULL,
            FOREIGN KEY (country_id) REFERENCES countries(id)
        )
    ''')

    # Create the places table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS places (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city_id INTEGER NOT NULL,
            FOREIGN KEY (city_id) REFERENCES cities(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
