import pymysql
import xlwt
from app.utils.XUtils import XUtils
from app.main.models.XAddress import XAddress


def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


def city_excel(city_name):
    excel_title = ['序号', '地址编号', '省份', '城市', '区/县', '乡', '详细地址（拼接省市区）', '详细地址(PROD地址)', '经度', '纬度']
    resource = 'resources/receiving_address_stock_1_ok.xls'
    stock_addr_list = XUtils.excel_to_list(p_read_excel_file_path=resource, p_sheet_name='Sheet1',p_excel_title_list=excel_title)
    length = len(stock_addr_list)
    write_data = []
    write_data.append(excel_title)
    for i in range(length):
        data = XAddress(stock_addr_list[i])
        if data.city_name == city_name:
            write_data.append(list(stock_addr_list[i].values()))
    if len(write_data) == 1:
        print('无可倒出内容')
    else:
        excel_name = '%s.xls' % city_name
        write_excel_xls(excel_name, 'Sheet1', write_data)

database = pymysql.connect(host="localhost", user="root", passwd="123456", db="mysql")
cursor = database.cursor()

# 创建插入SQL语句
query = "INSERT IGNORE INTO tpoint (row_id, location_id, province_name, city_name, district_name, town_name, location_name, " \
        "address, longitude, latitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

excel_title = ['序号', '地址编号', '省份', '城市', '区/县', '乡', '详细地址（拼接省市区）', '详细地址(PROD地址)', '经度', '纬度']
resource = 'resources/receiving_address_stock_1_ok.xls'
stock_addr_list = XUtils.excel_to_list(p_read_excel_file_path=resource, p_sheet_name='Sheet1', p_excel_title_list=excel_title)

l = len(stock_addr_list)
args = []
for i in range(l):
    data = XAddress(stock_addr_list[i])
    row_id = data.order
    location_id = data.address_no
    province_name = data.province_name
    city_name = data.city_name
    district_name = data.district_name
    town_name = data.town_name
    location_name = data.full_name
    address = data.full_name_prod
    longitude = data.longitude
    latitude = data.latitude
    values = (row_id, location_id, province_name, city_name, district_name, town_name, location_name, address, longitude, latitude)
    args.append(values)

# 执行sql语句
cursor.executemany(query, args)

# 关闭游标
cursor.close()

# 提交
database.commit()

# 关闭数据库连接
database.close()

# 打印结果
print("Done!")
city_excel('济南市')
city_excel('青岛市')
city_excel('123')

