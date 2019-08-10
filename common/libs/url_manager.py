class UrlManager(object):
    @staticmethod
    def build_url(path):
        return path

    @staticmethod
    def build_static_url(path):
        # 版本管理 ，在路由后面加上版本，防止前端静态文件缓存
        path = path + "?ver=20190807"
        return UrlManager.build_url(path)

