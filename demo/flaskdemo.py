from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql


app = Flask(__name__)
app.config["SQLAlCHEMY_DATABASE_URI"] = "mysql://root:mysqlpassword123@106.12.106.221/enxin"
#
db = SQLAlchemy(app)


@app.route("/")
def index():
    # from sqlalchemy import text
    # sql = text()
    db.create_all()
    result = db.engine.execute('SELECT * FROM haha')
    for row in result:
        app.logger.info(row)
    return "index"


@app.route("/a")
def a():

    # 打开数据库连接
    db = pymysql.connect("106.12.106.221", "root", "mysqlpassword123", "enxin")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * FROM haha")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    app.logger.info(data)

    # 关闭数据库连接
    db.close()

    return "index"


if __name__ == "__main__":
    app.debug = True
    app.run()