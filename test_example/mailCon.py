#mailCon.py
import imaplib

def connect_mail(mail_server,username, password):
    clint = imaplib.IMAP4(mail_server)
    rst=clint.login(username, password)
    return  rst

if __name__ == '__main__':
    mail126 = 'imap.126.com'
    mail163 = 'imap.163.com'
    m=connect_mail(mail163,'sun_jades','cails')
    print('mail:{},login:{},result:{}'.format(mail126,'cailinshan',m[0]))
