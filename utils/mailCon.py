#mailCon.py
import imaplib
import configs

def connect_mail(mailnm,user):
    sendserver = configs.mailinfo.get(mailnm).get('send')
    username = configs.mailinfo.get(mailnm).get(user).get('username')
    password = configs.mailinfo.get(mailnm).get(user).get('password')
    clint = imaplib.IMAP4(sendserver)
    rst=clint.login(username, password)
    return  rst

if __name__ == '__main__':
    mail126 = 'imap.126.com'
    mail163 = 'imap.163.com'
    m=connect_mail(mail163,'sun_jades','cails')
    print('mail:{},login:{},result:{}'.format(mail126,'cailinshan',m[0]))
