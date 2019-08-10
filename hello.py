from flask import Flask, url_for
from test_blueprint import testrouter
from common.libs.url_manager import UrlManager

app = Flask(__name__)
# 使用蓝牙路由功能，可以把api前缀相同的放到一个文件中，导入进来即可
app.register_blueprint(testrouter, url_prefix="/haha")


# 原生路由使用方式
@app.route("/")
def hello():
    # 根据方法名获取到路由地址
    url = url_for("index")
    # 根据地址管理器获取路由
    url1 = UrlManager.build_url("/index")
    # 使用build_static_url方法会在路由后面拼上版本
    url2 = UrlManager.build_static_url("/index.css")
    msg = "hello world,url=%s,url1=%s,url2=%s" % (url, url1, url2)
    app.logger.error(msg)
    # info 需要开启debug模式
    app.logger.info(msg)
    app.logger.debug(msg)
    return msg


@app.route("/index")
def index():
    return "index"


# 当请求的地址不存在，会在这统一处理
# 处理状态码是404的
@app.errorhandler(404)
def page_not_found(error):
    return "地址不存在"


if __name__ == "__main__":
    app.debug = True
    app.run()


