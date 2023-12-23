#!/home4/pagep82n/public_html/myenv/bin/python
import cgi
import mysql.connector
from mysql.connector import Error
import traceback

def log_error(error_message):
    with open("/home4/pagep82n/logs/cgi_error_log.txt", "w") as file:
        file.write(error_message + "\n")

def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS email_subscriptions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

print("Content-Type: text/html\n")
print("""
<html>
<head>
    <title>Email Subscription</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 40px; }
        .container { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        .message { color: green; }
        .error { color: red; }
    </style>
</head>
<body>
    <div class="container">
""")
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
        print("<p class='message'>Email saved successfully</p>")
    else:
        print("<p class='error'>No email provided</p>")

except Exception as e:
    print("<p class='error'>An error occurred.</p>")
    error_detail = traceback.format_exc()
    log_error(error_detail)

finally:
    print("</div>")
    print("</body></html>")
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
