'''
Excel表格数据处理工具
'''
import xlrd


def readRow(xls_name, row=0):
    '''
    read row's data
    :param row: the index of excel table
    :return: row_values
    '''
    book = xlrd.open_workbook(xls_name, 'r')
    table = book.sheet_by_index(0)
    return table.row_values(row)

print(readRow(r'../x.xls',1))
print('key[{}].value[{}]'.format(readRow(r'../x.xls',0)[0],readRow(r'../x.xls',0)[1]))
