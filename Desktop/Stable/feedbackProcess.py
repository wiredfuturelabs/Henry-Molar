import smtplib

def sendfeedback(name,mail,feedback):
	if str(name.get()) == "" or str(mail.get()) == "" or str(feedback.getAll()) == "":
		return "Please fill all field before send the mail"
	else:
		try:
			complete_body ="name:    " +  name.get() + "\nmail:   " + mail.get() + "\n\nfeedback:    " + str(feedback.getAll())
			EMAIL_ADRESS = "pythonprojectmail1@gmail.com"

			EMAIL_PASSWORD = "vrzdoskkghtvhyjv"
			SENDERSMAILID = "wiredfuturelabs.help@gmail.com"

			with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
				smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

				subject = "Feedback from Periodic Table"
				body = complete_body

				msg = f'subject:{subject}\n\n{body}'

				smtp.sendmail(EMAIL_ADRESS, SENDERSMAILID, msg)

			return "Feedback sent!"

		except:
			return "Feedback could not be sent, Please Try again."
