#配置文件：定义debug参数
#常量的话一般大写

# 适用于：存放用户密码、账号、app key
# git不要上传secure文件，因为涉及secure信息
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:lkjlkj@127.0.0.1:3306/fisher'
SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'