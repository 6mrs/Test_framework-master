import xlrd
from xlutils.copy import copy
import os

# 获取当前文件的绝对路径
curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
# 获取项目根目录
rootPath = os.path.abspath(os.path.dirname(curPath))
print(rootPath)


# 类中使用装饰器 @classmethod定义方法，是类方法
# 类中使用装饰器 @staticmethod定义方法，是静态方法


class Operate_Excel(object):
    """
    操作excel类

    """

    # 定义构造函数，创建对象自动执行
    def __init__(self, file_path=None, sheet_id=None):
        """

        :param file_path:如果没传值，默认为excel路径
        :param sheet_id:如果没传值，默认为第一个sheet页
        """
        if file_path:
            # 成员变量
            self.file_path = file_path
            self.sheet_id = sheet_id
        else:
            self.file_path = r'/Users/youjia/Desktop/Test_framework-master/data/api_data.xlsx'
            # 将文件目录拼接成绝对路径
            self.file_path = os.path.join(rootPath, self.file_path)
            print(self.file_path)

        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0
        # 调用成员方法
        self.sheet_table = self.get_sheet()

    """成员方法"""

    # 获取sheet页操作对象
    def get_sheet(self):
        data = xlrd.open_workbook(self.file_path)
        sheet_table = data.sheets()[self.sheet_id]
        return sheet_table

    # 获取sheet页的行数和列数，返回的是一个元组
    def get_sheet_nrows_ncols(self):
        return self.sheet_table.nrows, self.sheet_table.ncols

    # 获取sheet页的行数
    def get_sheet_nrows(self):
        return self.sheet_table.nrows

    # 获取sheet页的列数
    def get_sheet_ncols(self):
        return self.sheet_table.ncols

    # 获取具体单元格的数据
    def get_sheet_cell(self, row, col):
        """
        :params row: 单元格行值
        :params col: 单元格列值
        :return: cell_data
        """
        cell_data = self.sheet_table.cell_value(row, col)
        return cell_data

    # 写入数据到excel中
    def write_to_excel(self, row, col, values):
        # 打开excel文件读取数据句柄
        data = xlrd.open_workbook(self.file_path)
        # 复制excel
        copy_data = copy(data)
        # 读取复制的excel的sheet页
        copy_data_to_sheet = copy_data.get_sheet(0)
        # 通过get_sheet()获取的sheet有write()方法，写入数据
        copy_data_to_sheet.write(row, col, values)
        # 保存数据
        copy_data.save(self.file_path)


if __name__ == '__main__':
    read_xls = Operate_Excel()
    # print("获取excel表的行数与列数,返回元组格式: ", read_xls.get_sheet_nrows_ncols())
    # print("获取excel表的行数: ", read_xls.get_sheet_nrows())
    # print("获取excel表的列数: ", read_xls.get_sheet_ncols())
    # print("获取excel表的单元格(1,1)的值: ", read_xls.get_sheet_cell(1, 1))
    # print("获取excel表的单元格(1,2)的值: ", read_xls.get_sheet_cell(1, 2))
    # print("获取excel表的单元格(2,2)的值: ", read_xls.get_sheet_cell(2, 2))
    # print("写入excel表的单元格(2,2)的值: ", read_xls.write_to_excel(8, 8, 'test'))