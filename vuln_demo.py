import sqlite3
import sys

password = "SuperSecret123"  # Hardcoded secret
print(password)



def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable: unsanitized input directly in query
    query = "SELECT * FROM users WHERE name = '" + username + "';"
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

if __name__ == "__main__":
    get_user_data(sys.argv[1])

