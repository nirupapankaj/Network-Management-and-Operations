import smtplib
from scapy.all import rdpcap

#code to send email notification if a trap is recevied
to_email = 'nirupa.asokan@colorado.edu'
from_email = 'ashok.nirupa20@gmail.com'
username = 'winterfell'
password = ''
pack = rdpcap('tap0.pcap')
for item in pack:
	if (item.haslayer('UDP')):
		if (item['UDP'].dport == 162):
			server = smtplib.SMTP("smtp.gmail.com:587")
			server.starttls()
			server.login(username,password)
			message = "Issue: Trap received"
			server.sendmail(from_email, to_email, message)