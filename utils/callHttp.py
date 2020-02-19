import requests
import json
import utils.xlsData

def call_http(imethod, url, param={}):
    if imethod=='get':
        rst = requests.get(url, param)
    elif imethod == 'post':
        rst =requests.post(url,json.dumps(param))

    return rst

if __name__ == '__main__':
    pm = {'wd': 'python'}
    r = call_http('get','http://www.baidu.com/s',pm)
    print(r.status_code)

    rn = call_http('post','http://www.baidu.com/',pm)
    print('URL:{},status_code:{}\n{}'.format(rn.url,r.status_code,r.text))


'''
#读取url, param
url = utils.xlsData.readRow('../x.xls',0)[1]
param= utils.xlsData.readRow('../x.xls',1)[1]
rst = requests.get(url,params=param)
#r=requests.get(url='https://cart.taobao.com/trail_mini_cart.htm', params={'callback':'MiniCart.setData','t':'1526048972328'})
print('url:{0}\nparams:{1}'.format(url,param))
print('请求的URL为{0}\n返回状态：{1}'.format(rst.url,rst.status_code))
'''