import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)  # domain and port number
print(type(conn))

print(conn.ehlo())
conn.starttls()
conn.login('<email>', '<password>') # google has specific password (generate an App password)
conn.sendmail('<email>', '<email_recipient>', 'Subject: So long...\n\nDear Al, \nSo long, and thanks for all the fish.\n\n-Al')

conn.quit()