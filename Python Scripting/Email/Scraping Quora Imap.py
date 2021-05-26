import imapclient, pyzmail, requests, bs4, os
from urlextract import URLExtract
imapobj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapobj.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
imapobj.select_folder('INBOX', readonly=True)
#UIDs = imapobj.search('SUBJECT Digest')
Uids = imapobj.gmail_search(' Quora Digest')
mail_uid = Uids[(len(Uids)-1)]
#import pprint
#pprint.pprint(imapObj.list_folders())

rawMessages = imapobj.fetch([mail_uid], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessages[mail_uid][b'BODY[]'])
print(message.get_address('from'))

mail_text = message.text_part.get_payload().decode(message.text_part.charset)
extractor = URLExtract()
url = extractor.find_urls(mail_text)
#for i in range(len(url)):
    #webbrowser(url[i])
res = requests.get('%s' % (url[0]))
soup = bs4.BeautifulSoup(res.text, features='html.parser')
#print(soup.prettify())

#title = soup.find('title')
#print(title.getText())
#question = soup.find('script', type='application/ld+json')


imapobj.logout()
