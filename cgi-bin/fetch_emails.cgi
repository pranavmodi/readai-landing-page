#!/home4/pagep82n/public_html/myenv/bin/python
import mysql.connector
from mysql.connector import Error

def fetch_emails():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="pagep82n_pmodi",
            password="Topsecret11!!",
            database="pagep82n_emails"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT email, subscribed_at FROM email_subscriptions")

        print("Content-Type: text/html\n")
        print("<html><body>")
        print("<h1>Email Subscriptions</h1>")
        print("<ul>")
        for (email, subscribed_at) in cursor:
            print("<li>{}, Subscribed at: {}</li>".format(email, subscribed_at))
        print("</ul>")
        print("</body></html>")

        cursor.close()
        conn.close()

    except Error as e:
        print("Error: ", e)

fetch_emails()
