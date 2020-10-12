import pymysql
import xlrd


book = xlrd.open_workbook("resources/receiving_address_stock_1_ok.xls")
sheet = book.sheet_by_name("Sheet1")

database = pymysql.connect(host="localhost", user="root", passwd="123456", db="mysql")
cursor = database.cursor()

# 创建插入SQL语句
query = "INSERT INTO tpoint (rowid, locationId, provinceName, cityName, districtName, townName, locationName, " \
        "address, longitude, latitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

for r in range(1, sheet.nrows):
    rowid = sheet.cell(r, 0).value
    locationId = sheet.cell(r, 1).value
    provinceName = sheet.cell(r, 2).value
    cityName = sheet.cell(r, 3).value
    districtName = sheet.cell(r, 4).value
    townName = sheet.cell(r, 5).value
    locationName = sheet.cell(r, 6).value
    address = sheet.cell(r, 7).value
    longitude = sheet.cell(r, 8).value
    latitude = sheet.cell(r, 9).value
    values = (rowid, locationId, provinceName, cityName, districtName, townName, locationName, address, longitude, latitude)

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
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("我刚导入了{}列和{}行数据到MySQL!".format(columns, rows))