import flask
from 汉字转拼音 import hanzizhuanpinyin

app = flask.Flask(__name__)


@app.route('/excel')
def excelTool():
    content = 'test'
    keyword = flask.request.values.get('keyword', '')
    method = flask.request.values.get('method', '')
    print(keyword, method)
    if method == '帮助':
        content = """现在可以在第二个参数上输入‘帮助’，‘汉字转拼音’，
				‘手机号归属地’来获取第一个参数的相应信息，
				未来还将添加更多信……By Me醉嵩"""
    elif method == '汉字转拼音':
        content = hanzizhuanpinyin(keyword)
    return content

if __name__ == "__main__":
    app.run(host='0.0.0.0')
