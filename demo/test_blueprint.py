from flask import Blueprint
# Blueprint_test 随便命名
testrouter = Blueprint("Blueprint_test", __name__)


@testrouter.route("/test1")
def test1():
    return "test1"


@testrouter.route("/test2")
def test2():
    return "test2"

