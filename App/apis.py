# apis.py 文件定义各种api接口
'''
1.专门提供给客户端调用的接口
2.返回的数据一般是json格式的数据
'''
from flask_restful import Resource,fields,marshal_with,reqparse

# 蓝图 + 路由 + 视图函数 (FBV: function  base view)
# 类视图: (CBV: class  base  view)

# Resource:资源
class UserResource2(Resource):
    # 查
    def get(self):
        return {"name":"GET请求"}
    # 增
    def post(self):
        return {"name":"POST请求"}
    # 删
    def delete(self):
        return {"name":"DELETE请求"}
    # 改
    def put(self):
        return {"name":"PUT请求"}

# 对返回的数据进行验证: 字段格式化处理
user_fields = {
    'status':fields.Integer,
    'msg':fields.String,
    'data':fields.String,
    'data2':fields.String(default='李飞'),  # 设置返回数据的默认值
    'data4':fields.String(attribute='data3') # 隐藏返回的真实数据
}

class UserResource3(Resource):
    # 使用上面定义好的对字段的限制
    @marshal_with(user_fields)
    def get(self):
        return {
            'status':200,
            'msg':'ok',
            'data':'hello',
            'data3':'world'
        }

# 对返回的数据进行验证: 字段格式化处理
name_fields4 = {
    'name':fields.String,
    'age':fields.Integer,
    'sex':fields.String,
    #password 不返回
}
user_fields4 = {
    'status':fields.Integer,
    # 将显示的名称由msg改为message
    'message':fields.String(attribute='msg'),
    # 使用name_fileds4的限制
    'data':fields.Nested(name_fields4)
}

class UserResource4(Resource):
    # 此处的装饰器只能传输一个参数
    @marshal_with(user_fields4)
    def get(self):
        return {
            'status':200,
            'msg':'ok',
            'data':{
                'name':'马斯克',
                'age':42,
                'sex':'男',
                'password':12345
            }
        }
# 请求参数的解析:浏览器传输到服务端的数据做预处理
# http://127.0.0.1:5000/user5/?name = '张三'

parser = reqparse.RequestParser()
parser.add_argument('name',type=str,required=True,help='name是必须参数')
class UserResource5(Resource):
    def get(self):
        args = parser.parse_args()
        # 获取url地址栏中的参数
        name = args.get('name')
        print("传递的name参数是:",name)
        return {'msg':name}
