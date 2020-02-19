import requests

def baidu_open():
    url='http://www.baidu.com'
    rst = requests.get(url)
    print('test_baidu_open->url:{}'.format(url))
    return rst

def baidu_search():
    url='http://www.baidu.com/s'
    pm = {'wd':'python'}
    print('test_baidu_search->url:{}'.format(url))
    rst = requests.get(url, pm)
    return rst

if __name__ == '__main__':
    baidu_open()
    baidu_search()