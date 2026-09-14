import smtplib

sender_email="bookwarm2012@gmail.com"
receiver_email="musarratahona@gmail.com"
app_password="rtlv ykxh fsdy usul"

subject="Harry Potter and the Goblet of Fire review"
body="There will be three task,spaced throuhout the school year.Only wizards who are over seventeen are allowed to enter Triwizard Tournament.But somehow Goblet chose Harry.Harry was amazed to find his name.He will face death-defying task.But with help of his friends he made it through alive."

message=f"Subject:{subject}\n\n{body}"

try:
    print("Connecting  to the SMTP server...")
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()


    print("Logging in to the SMTP server...")
    server.login(sender_email,app_password)

    print("Sending the email...")
    server.sendmail(sender_email,receiver_email,message)
    print("Email sent successfully...")

except Exception as e:
    print(f"Error:{e}")

finally:
    server.quit()