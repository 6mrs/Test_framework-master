from test.interface.basic_method import get_case_header, get_case_is_execute, get_case_interface_url, get_case_method, \
    get_case_payload, get_case_actual_result, get_case_expected_result, get_case_name
from test.interface.read_excel import Operate_Excel


class getData(object):
    def __init__(self):
        self.op_excel = Operate_Excel()

    def get_case_nums(self):
        """获取测试用例条数"""
        return self.op_excel.get_sheet_nrows()

    def get_is_header(self, row):
        """是否携带请求头"""
        col = int(get_case_header())
        header = self.op_excel.get_sheet_cell(row, col)
        if header is not None:
            return header
        else:
            print("没有header！")
            return None

    def get_is_run(self, row):
        """是否运行"""
        col = int(get_case_is_execute())
        is_run = self.op_excel.get_sheet_cell(row, col)
        if is_run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def get_name(self, row):
        """获取测试名称"""
        col = int(get_case_name())
        name = self.op_excel.get_sheet_cell(row, col)
        return name

    def get_url(self, row):
        """获取url"""
        col = int(get_case_interface_url())
        url = self.op_excel.get_sheet_cell(row, col)
        return url

    def get_method(self, row):
        """获取请求方法"""
        col = int(get_case_method())
        method = self.op_excel.get_sheet_cell(row, col)
        return method

    def get_data(self, row):
        """获取请求数据"""
        col = int(get_case_payload())
        data = self.op_excel.get_sheet_cell(row, col)
        return data

    def get_excepted_result(self, row):
        """获取预期结果"""
        col = int(get_case_expected_result())
        excepted_result = self.op_excel.get_sheet_cell(row, col)
        if excepted_result == '':
            return None
        else:
            return excepted_result

    def get_actual_result(self, row, value):
        """获取实际结果"""
        col = int(get_case_actual_result())
        actual_result = self.op_excel.get_sheet_cell(row, col)
        self.op_excel.write_to_excel(row, col, value)


if __name__ == '__main__':
    get_data = getData()
