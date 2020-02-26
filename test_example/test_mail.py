import sys
sys.path.append('..')
from utils import mailCon
import configs

def test_126():
    rst = mailCon.connect_mail('126.com', 'cails')
    assert rst[0]=='OK'
    return rst

def test_163():
    rst = mailCon.connect_mail('163.com', 'cails')
    assert rst[0] == 'OK'
    return rst
def test_asiainfo():
    rst = mailCon.connect_mail('asiainfo.com', 'caixg')
    assert rst[0] == 'OK'
    return rst

if __name__ == '__main__':
    print('126.com,cails login:{}'.format(test_126()[0]))
    print('163.com,cails login:{}'.format(test_163()[0]))
    print('asiainfo.com,caixg login:{}'.format(test_asiainfo()[0]))

