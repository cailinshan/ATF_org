import requests
import sys
sys.path.append("..")
import utils.callHttp

def test_baidu_open():
    assert utils.callHttp.call_http('get', 'http://www.baidu.com').status_code==200

def test_www_asiainfo_open():
    assert utils.callHttp.call_http('get', 'http://www.asiainfo.com').status_code==200

def test_oa_asiainfo_open():
    assert utils.callHttp.call_http('get', 'http://oa.asiainfo.com').status_code==200

def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 1
def test_function(record_property):
    record_property("example_key", 1)
    assert True