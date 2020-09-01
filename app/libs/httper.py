# 可以用urllib发送http请求： from urllib import request
# 用requests第三方库发送: 需要安装

import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # r是requests请求结果的一个封装，并不是最终结果
        # 外部的API大都是：restful api返回的结果一定要是json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
