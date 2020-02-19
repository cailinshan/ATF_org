import mailCon

def test_126():
    rst = mailCon.connect_mail('imap.126.com','cailinshan','cails')
    assert rst[0]=='OK'

def test_163():
    rst = mailCon.connect_mail('imap.163.com', 'sun_jades', 'cails')
    assert rst[0] == 'ok'
