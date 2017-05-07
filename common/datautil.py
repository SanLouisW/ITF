#coding=utf-8

import xlrd
import os
from xlutils.copy import copy as copy
from xlwt import easyxf, Workbook


class ExcelLibrary:

    def __init__(self,filename):
        # type: (object) -> object
        self.wb = xlrd.open_workbook(filename,formatting_info=True)
        self.fileName = filename
        self.tb = None
        self.sheetNames = self.wb.sheet_names()

    def get_column_count(self, sheetname):
        sheet = self.wb.sheet_by_name(sheetname)
        return sheet.ncols


    def get_row_count(self, sheetname):
        sheet = self.wb.sheet_by_name(sheetname)
        return sheet.nrows

    def get_data(self,rowValue,colValue,sheetname=''):
        """
        :param rowValue:表格的行
        :param colValue: 表格的列
        :param sheetname: sheetname
        :param file_name: excel文件
        :return:
        """
        sheet=self.wb.sheet_by_name(sheetname)
        return sheet.cell_value(rowValue,colValue)


    # '''
    # 获取对应的url
    # '''
    # def get_request_url(self,sheetname,index,column=0):
    #     row_counts = self.get_row_count(sheetname)
    #     for row in range(1, row_counts):
    #         return_index = self.get_data(row, column,sheetname)
    #         if return_index == index:
    #             request_url = self.get_data(row, 2, sheetname)
    #             return request_url.strip()
    #
    #     raise Exception("can't find this index.")
    #
    #
    # '''
    # 获取对应的body
    # '''
    # def get_request_body(self,sheetname,testcase_id,column=0):
    #     row_counts = self.get_row_count(sheetname)
    #     for row in range(1, row_counts):
    #         return_testcase_id = self.get_data(row, column,sheetname)
    #         if return_testcase_id == testcase_id:
    #             request_body = self.get_data(row, 5, sheetname)
    #             return str(request_body).strip()
    #
    #     raise Exception("can't find this index.")

    # '''
    # 获取预期返回结果
    # '''
    # def get_except_result(self,sheetname,testcase_id,column=0):
    #     row_counts = self.get_row_count(sheetname)
    #     for row in range(1, row_counts):
    #         return_testcase_id = self.get_data(row, column,sheetname)
    #         if return_testcase_id == testcase_id:
    #             except_result = self.get_data(row, 6, sheetname)
    #             return str(except_result).strip()
    #
    #     raise Exception("can't find this index.")

    # '''
    # 设置执行结果
    # '''
    #
    # def set_result(self,result, testcase_id, sheetname, column=0):
    #
    #     row_counts = self.get_row_count(sheetname)
    #     my_sheet_index = self.sheetNames.index(sheetname)
    #     for row in range(1, row_counts):
    #         return_testcase_id = self.get_data(row, column,sheetname)
    #         if return_testcase_id == testcase_id:
    #             if result == 'Pass':
    #                 tittle_style = easyxf('font: height 300, name SimSun, colour_index green, bold on; align: wrap on, vert centre, horiz center;')
    #             else:
    #                 tittle_style = easyxf('font: height 300, name SimSun, colour_index red, bold on; align: wrap on, vert centre, horiz center;')
    #             self.tb = copy(self.wb)
    #             self.tb.get_sheet(my_sheet_index).write(row,7,result,tittle_style)
    #             # self.tb.save(self.fileName)
    #             self.wb = xlrd.open_workbook(self.fileName,formatting_info=True)
    #             break

    '''
    获取case所在的行
    '''
    def get_case_row(self,sheetname,testcase_id,column=0):
        row_counts = self.get_row_count(sheetname)
        for row in range(1, row_counts):
            return_testcase_id = self.get_data(row, column,sheetname)
            if return_testcase_id == testcase_id:
                return row

        raise Exception("can't find this index.")

    '''
    获取url
    '''
    def get_request_url(self,sheetname,row, column=2):
            return_url = self.get_data(row, column,sheetname)
            return return_url

    '''
    获取body
    '''
    def get_request_body(self,sheetname,row, column=5):

            return_body = self.get_data(row, column,sheetname)
            return return_body

    '''
    获取header
    '''
    def get_request_headers(self,sheetname,row, column=3):

            return_header = self.get_data(row, column,sheetname)
            return return_header

    '''
    获取预期结果
    '''
    def get_except_result(self,sheetname, row, column=6):
            return_except_result = self.get_data(row, column,sheetname)
            return return_except_result.strip()

    '''
    设置执行结果
    '''

    def set_result(self,result, sheetname, row, column=7):

        my_sheet_index = self.sheetNames.index(sheetname)

        if result == 'Pass':
            tittle_style = easyxf('font: height 300, name SimSun, colour_index green, bold on; align: wrap on, vert centre, horiz center;')
        else:
            tittle_style = easyxf('font: height 300, name SimSun, colour_index red, bold on; align: wrap on, vert centre, horiz center;')
        self.tb = copy(self.wb)
        self.tb.get_sheet(my_sheet_index).write(row,column,result,tittle_style)
        self.tb.save(self.fileName)
        self.wb = xlrd.open_workbook(self.fileName,formatting_info=True)


if __name__ == '__main__':
    e = ExcelLibrary('./commons_weixin_api.xls')
    e.set_result('Pass','user_register',1)
    # e.set_result('Pass','ddkl_IT_dynamic_create_002','dynamic_create')
    # print e.get_column_count('Sheet1')
    # print e.get_data(0,0,'Sheet1')
    # e.get_data(10,10,'Sheet1')
    # print e.get_request_url('Sheet1','ddkl_IT_user_register_001')
    # row = e.get_case_Id('Sheet1','ddkl_IT_user_register_001')
    # print row
    # print e.get_request_url('Sheet1',row)
    # print e.get_request_url('Sheet1',row+1)
    # print e.get_request_url('Sheet1',row+2)
    # print e.get_request_body('Sheet1',row)
    # print e.get_request_body('Sheet1',row+1)
    # print e.get_request_body('Sheet1',row+2)
    # print e.get_request_body('Sheet1','index_notify_get_notify_details')
    # print type(e.get_request_body('Sheet1','index_notify_get_notify_details'))




















#
# if __name__ == '__main__':
#     print get_data(0,1,'Sheet1')