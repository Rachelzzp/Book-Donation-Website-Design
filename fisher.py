from app import create_app

# app: flask实例化，可加入插件、配置文件等
app = create_app()


# 保证web是在入口文件运行的
if __name__ == '__main__':
    # print(str(id(app)) + 'id启动')
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=82, threaded=True)

    # 生产环境中，实际是nginx接受浏览器发来的请求后，转发给uwsgi（web服务器），加载fisher模块启动flask相关代码
    # 浏览器 -> nginx -> uwsgi -> 加载设计的模块 -> 启动flask代码

    # 相当于mvc中的视图函数
    # 基于类的视图，即插视图（如果是基于函数的话，很难实现代码的复用，而类是可以继承的）
    # route装饰器路由注册方法一
    # response = make_response('<html></html>', 404)
    # response.headers = headers
    # return response
    # 路由注册方法二（当基于类的视图时，只能用add_url_rule）： app.add_url_rule('/zrc', view_func=hello())
    # 开启debug可以自动重启，不用每次更新文件后都要terminal重新运行，并且出错会显示在网页上

