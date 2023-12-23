#!/home4/pagep82n/public_html/myenv/bin/python
import cgi
import mysql.connector
from mysql.connector import Error

def log_error(error_message):
    with open("/home4/pagep82n/logs/cgi_error_log.txt", "w") as file:
        file.write(error_message + "\n")

def create_table(cursor):
    print("<p>creating table</p>")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_subscriptions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

print("Content-Type: text/html\n")
print("<html><body>")

try:
    form = cgi.FieldStorage()
    email = form.getvalue('email')

    conn = mysql.connector.connect(
        host="localhost",
        user="pagep82n_pmodi",
        password="Topsecret11!!",
        database="pagep82n_emails"
    )
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    create_table(cursor)

    if email:
        cursor.execute("INSERT INTO email_subscriptions (email) VALUES (%s)", (email,))
        conn.commit()
        print("<p>Email saved successfully</p>")
    else:
        print("<p>No email provided</p>")

except Exception as e:
    print("<p>An error occurred.</p>")
    error_detail = traceback.format_exc()
    log_error(error_detail)

finally:
    print("<p>hello finally</p>")
    print("</body></html>")
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()