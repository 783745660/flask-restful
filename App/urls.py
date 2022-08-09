# urls.py 主要是控制各种路由.  不需要使用蓝图文件了
from App.exts import api
from App.apis import * 


# 写各种路由    api.add_resource(apis中的类名,路由)
api.add_resource(UserResource2,'/user2/')
api.add_resource(UserResource3,'/user3/')
api.add_resource(UserResource4,'/user4/')

api.add_resource(UserResource5,'/user5/')