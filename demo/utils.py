import hashlib,base64

""""
md5 加密方法
"""


class Md5Service:
    @staticmethod
    def toMd5Str(str, salt):
        ss = "%s%s" % (base64.encodebytes(str.encode("utf-8")), salt)
        m = hashlib.md5()
        m.update(ss.encode("utf-8"))
        return m.hexdigest()


print(Md5Service.toMd5Str("123", "a"))

