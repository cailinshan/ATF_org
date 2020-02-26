from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

class WebserviceTest:
    def __init__(self,url):
        #下面的3行为了解决下面的错误 suds.TypeNotFound: Type not found: '(schema, http://www.w3.org/2001/XMLSchema, )'
        imp = Import('http://www.w3.org/2001/XMLSchema',location = 'http://www.w3.org/2001/XMLSchema.xsd')
        imp.filter.add('http://WebXml.com.cn/')
        doctor = ImportDoctor(imp)
        self.client = Client(url,doctor=doctor)
    #获取方法名称
    def get_methods_name(self):
        method_list=[]
        for i in self.client.wsdl.services[0].ports[0].methods:
            method_list.append(i)
        return  method_list
    #获取方法参数
    def get_method_params(self, method_name):
        method = self.client.wsdl.services[0].ports[0].methods[method_name]
        input_params = method.binding.input
        return input_params.param_defs(method)

    def run_main(self):
        for method in self.get_methods_name():
            func = getattr(self.client.service, method)
default_values = {'username':'caixg','password':'cails_123', 'suit':{'case1':'weather_forecast','test2':'TV-view'}}
if __name__ == '__main__':
    print(default_values.get('username'))
    print(default_values.get('suit').get('test2'))
    exit(1)

    url = 'http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl'
    web = WebserviceTest(url)
    methods = web.get_methods_name()
    list_m = list(methods)
    print(list_m)
    #输出每个方法的key、values
    for i in range(0,len(methods)):
        print('第{}个method：{},参数:\n{}'.format(i,list_m[i], web.get_method_params(list_m[i])))
