import pymysql
import xlwt
from app.utils.XUtils import XUtils


def export_excel(sql, excel_name, cur, conn):
    # 连接数据库，查询数据
    # cur.execute(sql)  # 返回受影响的行数
    XUtils.execute_sql(p_sql=sql, p_cur=cur, p_conn=conn)

    fields = [field[0] for field in cur.description]  # 获取所有字段名
    # all_data = cur.fetchall()  # 所有数据
    success, all_data = XUtils.fetchall_sql(p_sql=sql, p_cur=cur)

    # 写入excel
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')

    for col, field in enumerate(fields):
        sheet.write(0, col, field)

    row = 1
    for data in all_data:
        for col, field in enumerate(data):
            sheet.write(row, col, field)
        row += 1
    book.save("%s.xls" % excel_name)






if __name__ == '__main__':
    # host, user, passwd, db = '127.0.0.1', 'root', '123456', 'mysql'
    # conn = pymysql.connect(user=user, host=host, port=3306, passwd=passwd, db=db, charset='utf8')
    # cur = conn.cursor()
    conn_success, conn, cur = XUtils.db_connect_with_pymysql(p_user='root', p_host='127.0.0.1', p_passwd='123456', p_db_name='mysql', p_charset='utf8')
    if conn_success:
        print('sql success connect')
    table_name = 'tpoint'
    query = 'select * from %s' % table_name
    city_name = '青岛市'
    query_1 = "SELECT DISTINCT * FROM tpoint t WHERE t.city_name = '" + city_name + "'"
    export_excel(query, 'tpoint', cur, conn)
    export_excel(query_1, '青岛市', cur, conn)
    XUtils.db_close(p_cursor=cur, p_conn=conn)
    # cur.close()
    # conn.close()

