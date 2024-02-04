import smtplib
my_email = "test@gmail.com"
password = "test@1234"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail(
    from_addr=my_email,
    to_addrs="recipeintemail@gmail.com",
    msg="Hello WOrld! This is a test message!"
)

connection.close()
