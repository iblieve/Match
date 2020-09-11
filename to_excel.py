import xlwt


def list_to_excel(title_list=None, addr_list=None, sheet_name: str = None, a: int = None, b: int = None) -> (bool):
    """
    将列表写入Excel中
    title_list 列标题
    a 起始数字
    b 终止数字
    """
    to_excel = [title_list]
    book = xlwt.Workbook()
    sheet = book.add_sheet(sheet_name)
    row_index = 0
    for i in range(a,b):
        sing_address = []
        for value in addr_list[i].values():
            sing_address.append(value)
        to_excel.append(sing_address)

    for i in range(len(to_excel)):
        col_index = 0
        for val in to_excel[i]:
            sheet.write(row_index, col_index, val)
            col_index += 1
        row_index += 1
    book.save("top_10.xls")








