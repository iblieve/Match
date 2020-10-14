import pymysql
from app.utils.XUtils import XUtils
from app.main.models.XAddress import XAddress


database = pymysql.connect(host="localhost", user="root", passwd="123456", db="mysql")
cursor = database.cursor()

# 创建插入SQL语句
query = "INSERT IGNORE INTO tpoint (row_id, location_id, province_name, city_name, district_name, town_name, location_name, " \
        "address, longitude, latitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

excel_title = ['序号', '地址编号', '省份', '城市', '区/县', '乡', '详细地址（拼接省市区）', '详细地址(PROD地址)', '经度', '纬度']
resource = 'resources/receiving_address_stock_1_ok.xls'
stock_addr_list = XUtils.excel_to_list(p_read_excel_file_path=resource, p_sheet_name='Sheet1', p_excel_title_list=excel_title)

l = len(stock_addr_list)
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

    # 执行sql语句
    cursor.execute(query, values)

# 关闭游标
cursor.close()

# 提交
database.commit()

# 关闭数据库连接
database.close()

# 打印结果
print("Done!")

