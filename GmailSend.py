#! /usr/bin/python3.9
#imports
from util import *
import smtplib

#main
def Main(argv):
	argk = list(argv.keys())
	def	get(*indicators):
		nonlocal argv,argk
		other = []
		for indicator in indicators:
			if indicator in argk:
				other.append(argv[indicator])
		return other

	# get passwd & addr
	email = getenv("GmailAddr")
	passwd = getenv("GmailPassword")

	try:

		# with smtplib.SMTP("smtp.gmail.com", 587) as server:
			# server.ehlo()

			# # encrypt
			# server.starttls()

			# # make sure it's workin
			# server.ehlo()

			# server.login(email, passwd)

			# subject = get("-s","-S","--subject","-h","-H","--header")
			# body = get("-c","-C","--content","-b","-B","--body")
			# to = get("-t","-T","-to")

			# msg = "Subject: %s\n\n%s" % (subject,msg)

			# server.sendmail(email, to, msg)
		sleep(1.4)
	except Exception:
		return 1



	return 0


#start
if __name__ == '__main__':
	argv = ArgvAssing(argv[1:])
	start = tm()
	ExitCode = Main(argv)

	if '--debug' in argv.keys():
		if not ExitCode:printl("%scode successfully exited in " % color["green"])
		else:printl("%scode exited with error %f in " % (color["red"],ExitCode))
		print("%.3f seconds%s" % (round(tm()-start,5),color["nc"]))
	exit(ExitCode)
