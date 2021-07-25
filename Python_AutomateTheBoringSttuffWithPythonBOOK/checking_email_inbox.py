import imapclient
conn = imapclient.IMAPClient('imap.gmail.com', ssl = True)
# ssl is an encription algorithm
conn.login('<email>', '<password>')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE 20-Aug-2015'])
print(UIDs)
conn.fetch([47474], ['BODY[]', 'FLAGS'])
rawMessage = conn.fetch([47474],['BODY[]', 'FLAGS'])
import pyzmail
pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')
message.text_part
message.text_part == None
message.text_part.get_playload().code('UTF-8')
message.text_part.charset
message.text_part.charset == None
conn.list_folders()
conn.select_folder('<folder>', readonly=False)
UIDs= conn.search[('ON 24-Aug-2015')]
UIDs
conn.delete_messaged([UIDs])