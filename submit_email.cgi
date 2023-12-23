#!/home4/pagep82n/public_html/myenv/bin/python
import cgi
import mysql.connector
from mysql.connector import Error
import traceback

# Function to log errors to a file
def log_error(error_message):
    with open("/home4/pagep82n/logs/cgi_error_log.txt", "a") as file:
        file.write(error_message + "\n")

print("Content-Type: text/html\n")
print("<html><body>")

try:
    form = cgi.FieldStorage()
    email = form.getvalue('email')

    if email:
        print("<p>Email: {}</p>".format(email))

        conn = mysql.connector.connect(
            host="localhost",
            user="pagep82n_pmodi",
            password="Topsecret11!!",
            database="pagep82n_emails"
        )
        cursor = conn.cursor()
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
    print("</body></html>")
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()



# print("Content-Type: text/html\n")
# print("<html><body>")
# print("<p>Hello, World!</p>")

# import cgi
# form = cgi.FieldStorage()
# email = form.getvalue('email')

# if email:
#     print("<p>Email: {}</p>".format(email))
# else:
#     print("<p>No email provided</p>")

# print("</body></html>")

