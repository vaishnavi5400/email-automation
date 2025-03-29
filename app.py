# import logging
# from flask import Flask, render_template, request, redirect, flash
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import os
# import schedule
# import time
# from dotenv import load_dotenv
# import threading

# # Load environment variables
# load_dotenv()

# # Define email-related environment variables
# EMAIL_HOST=os.getenv("EMAIL_HOST")
# EMAIL_PORT=os.getenv("EMAIL_PORT")
# EMAIL_USER=os.getenv("EMAIL_USER")
# EMAIL_PASS=os.getenv("EMAIL_PASS")

# # Use the environment variables
# SMTP_SERVER = EMAIL_HOST
# SMTP_PORT = 587
 
# logging.basicConfig(
#     filename="email_logs.log",  # Log file
#     level=logging.INFO,  # Log INFO & ERROR messages
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )
# app = Flask(__name__)
# app.secret_key = os.getenv("SECRET_KEY")


# EMAIL_HOST = os.getenv("EMAIL_HOST")
# EMAIL_PORT = os.getenv("EMAIL_PORT")
# EMAIL_USER = os.getenv("EMAIL_USER")
# EMAIL_PASS = os.getenv("EMAIL_PASS")

# # Function to send an email
# def send_email(to_email, subject, message):
#     try: 
#      msg = MIMEMultipart()
#      msg["From"] = EMAIL_USER
#      msg["To"] = to_email
#      msg["Subject"] = subject
#      msg.attach(MIMEText(message, "html"))

#      server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#      server.starttls()
#      server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#      server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
#      server.quit()
#      logging.info(f"Email sent to {to_email} | Subject: {subject}")
#      print("Email sent successfully")
#     except Exception as e:
#         print(f"Failed to send email. Error: {e}")


# # Flask route to render the HTML form
# @app.route("/")
# def index():
#     return render_template("index.html")

# # Handle form submission
# @app.route("/send_email", methods=["POST"])
# def send_email_route():
#     try:
#         print(" Received email request!")

#         to_email = request.form["email"]
#         subject = request.form["subject"]
#         message = request.form["message"]

#         print(f"Sending to: {to_email}, Subject: {subject}")

#         send_email(to_email, subject, message)

#         print("Email sent successfully!")
#         flash("Email sent successfully!", "success")
#         return redirect("/")
    
#     except Exception as e:
#         print(f" Error: {e}")
#         flash(f"Error: {e}", "danger")
#         return redirect("/")

# # Schedule an automated email (Runs at 9 AM daily)
# def scheduled_task():
#     send_email(EMAIL_USER, "Scheduled Email", "<p>This is an automated email.</p>")

# schedule.every().day.at("09:00").do(scheduled_task)

# # Function to run the scheduler in a separate thread
# def run_scheduler():
#     while True:
#         schedule.run_pending()
#         time.sleep(60)

# # Start the scheduler in a background thread
# scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
# scheduler_thread.start()

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)
# os.environ["FLASK_RUN_EXTRA_FILES"] = "app.py"


# import logging
# from flask import Flask, render_template, request, redirect, flash
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import os
# import schedule
# import time
# from dotenv import load_dotenv
# import threading

# # Load environment variables
# load_dotenv()

# # Define email-related environment variables
# EMAIL_HOST = os.getenv("EMAIL_HOST")
# EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))  # Convert PORT to integer
# EMAIL_USER = os.getenv("EMAIL_USER")
# EMAIL_PASS = os.getenv("EMAIL_PASS")
# SECRET_KEY = os.getenv("SECRET_KEY")

# # Debugging info to check if environment variables are loaded
# print(f"EMAIL_USER: {EMAIL_USER}, EMAIL_PASS: {'Loaded' if EMAIL_PASS else 'Not Loaded'}")

# # Use the environment variables
# SMTP_SERVER = EMAIL_HOST
# SMTP_PORT = EMAIL_PORT

# # Configure logging
# logging.basicConfig(
#     filename="email_logs.log",  # Log file
#     level=logging.INFO,  # Log INFO & ERROR messages
#     format="%(asctime)s - %(levelname)s - %(message)s",
# )

# app = Flask(__name__)
# app.secret_key = SECRET_KEY  # Use SECRET_KEY from .env

# # Function to send an email
# def send_email(to_emails, subject, message):
#     try: 
#         msg = MIMEMultipart()
#         msg["From"] = EMAIL_USER
#         msg["To"] = ", ".join(to_emails)  # Combine multiple emails
#         msg["Subject"] = subject
#         msg.attach(MIMEText(message, "html"))

#         server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#         server.starttls()
#         server.login(EMAIL_USER, EMAIL_PASS)  # Corrected variable usage
        
#         for email in to_emails:
#             server.sendmail(EMAIL_USER, email, msg.as_string())

#         server.quit()

#         logging.info(f"Email sent to {', '.join(to_emails)} | Subject: {subject}")
#         print("Emails sent successfully")
#     except Exception as e:
#         logging.error(f"Failed to send emails. Error: {e}")
#         print(f"Failed to send emails. Error: {e}")

# # Flask route to render the HTML form
# @app.route("/")
# def index():
#     return render_template("index.html")

# # Handle form submission
# @app.route("/send_email", methods=["POST"])
# def send_email_route():
#     try:
#         print("Received email request!")

#         # Get multiple email addresses as a list
#         to_emails = request.form["email"].split(",")  
#         to_emails = [email.strip() for email in to_emails]  # Remove extra spaces

#         subject = request.form["subject"]
#         message = request.form["message"]

#         print(f"Sending to: {', '.join(to_emails)}, Subject: {subject}")

#         # Send email to multiple recipients
#         send_email(to_emails, subject, message)

#         print("Emails sent successfully!")
#         flash("Emails sent successfully!", "success")
#         return redirect("/")
    
#     except Exception as e:
#         logging.error(f"Error: {e}")
#         print(f"Error: {e}")
#         flash(f"Error: {e}", "danger")
#         return redirect("/")

# # Schedule an automated email (Runs at 9 AM daily)
# def scheduled_task():
#     send_email([EMAIL_USER], "Scheduled Email", "<p>This is an automated email.</p>")

# schedule.every().day.at("09:00").do(scheduled_task)

# # Function to run the scheduler in a separate thread
# def run_scheduler():
#     while True:
#         schedule.run_pending()
#         time.sleep(60)

# # Start the scheduler in a background thread
# scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
# scheduler_thread.start()

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)
 
import os
import csv
import smtplib
import json
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER", "static/uploads")
app.secret_key = "supersecretkey"

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Function to send email
def send_email(name, recipient, subject, message, attachment_path):
    try:
        sender_email = os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASS")

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        # Attach file if exists
        if attachment_path:
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}")
                msg.attach(part)

        # Send email
        server = smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT")))
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        
        flash("Email sent successfully!", "success")

    except Exception as e:
        flash(f"Failed to send email: {str(e)}", "danger")

# Function to read emails from CSV
def load_csv_data():
    email_data = []
    csv_file = "emails.csv"
    
    if os.path.exists(csv_file):
        with open(csv_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row:
                    email_data.append(row)
    
    return email_data

@app.route("/", methods=["GET", "POST"])
def index():
    email_data = load_csv_data() 
    if not email_data:
        email_data = []
    return render_template("index.html", email_data=email_data or [])  # Ensure it's not None
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
@app.route("/send_email", methods=["POST"])
def send():
    name = request.form.get("name")
    recipient = request.form.get("recipient")
    subject = request.form.get("subject")
    message = request.form.get("message")

    # Handle file upload
    attachment_path = None
    if "attachment" in request.files:
        file = request.files["attachment"]
        if file.filename != "":
            filename = secure_filename(file.filename)
            attachment_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(attachment_path)

    # Send email
    send_email(name, recipient, subject, message, attachment_path)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

