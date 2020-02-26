import sys
sys.path.append("..")
import utils.callWS
from suds import sudsobject

lurl='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl'
def wea_forecast(url=lurl,city_id=1384):
    web = utils.callWS.WebserviceTest(url)
    wea_rst = web.client.service.getWeather(theCityCode=city_id)
    wea_dict = sudsobject.asdict(wea_rst)
    wea_list = wea_dict.get('%s'%'string')
    return  wea_list

def test_zhengzhou():
    assert len(wea_forecast(city_id=539)) > 10

if __name__ == '__main__':
    print(wea_forecast(city_id=539))