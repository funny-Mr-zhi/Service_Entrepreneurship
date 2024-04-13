
from flask import Flask, request, send_file, make_response,jsonify
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://yiyan.baidu.com"}})

app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB


def make_json_response(data, status_code=200):
    response = make_response(json.dumps(data), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


# @app.route("/add_word", methods=['POST'])
# async def add_word():
#     """
#         添加一个单词
#     """
#     word = request.json.get('word', "")
#     wordbook.append(word)
#     return make_json_response({"message": "单词添加成功"})



# # --lzy change in 4.12
# @app.route("/upload_file", methods=["GET", "POST"])
# async def upload_file():
#     # 检查请求中是否包含文件
#     print("hello world!")
#     if "file" not in (await request.files):
#         return make_response(jsonify({"status": "error", "message": "No file provided"}), 400)

#     # 从请求中获取文件对象
#     file = await request.files["file"]

#     # 保存文件或进行其他操作
#     # 这里只是简单地打印文件名和内容
#     print("文件名:", file.name)
#     print("文件内容:", file.read())

#     # 返回成功响应
#     return make_response(jsonify({"status": "success", "message": "文件上传成功"}), 200)

# @app.route("/upload_file", methods=["POST"])
# async def upload_file():
#     print("hello world!")
#     # 检查请求中是否包含文件
#     if "file" not in request.files:
#         print("No file provided")
#         return make_response(jsonify({"status": "error", "message": "No file provided"}), 400)

#     # 从请求中获取文件对象
#     file = request.data["file"]

#     # 保存文件或进行其他操作
#     # 这里只是简单地打印文件名和内容
#     print("文件名:", file.name)
#     print("文件内容:", file.read())

#     # 返回成功响应
#     return make_response(jsonify({"status": "success", "message": "文件上传成功"}), 200)

@app.route("/upload_file", methods=["POST"])
async def upload_file():
    print("hello world!")
    
    # 输出函数内部的所有内容
    print("函数内部内容:")
    print(upload_file.__code__.co_consts[0])  # 输出函数定义的第一行内容
    
    # 输出请求对象的所有内容
    print("请求对象的所有内容:")
    print(request.__dict__)  # 输出请求对象的所有属性和值
    
    # 检查请求中是否包含文件
    if "file" not in request.files:
        print("No file provided")
        return make_response(jsonify({"status": "error", "message": "No file provided"}), 400)

    # 从请求中获取文件对象
    file = request.files["file"]

    # 保存文件或进行其他操作
    # 这里只是简单地打印文件名和内容
    print("文件名:", file.filename)
    print("文件内容:", file.read())

    # 返回成功响应
    return make_response(jsonify({"status": "success", "message": "文件上传成功"}), 200)


@app.route("/.well-known/ai-plugin.json")
async def plugin_manifest():
    """
        注册用的：返回插件的描述文件，描述了插件是什么等信息。
        注意：API路由是固定的，事先约定的。
    """
    host = request.host_url
    with open(".well-known/ai-plugin.json", encoding="utf-8") as f:
        text = f.read().replace("PLUGIN_HOST", host)
        return text, 200, {"Content-Type": "application/json"}



@app.route("/.well-known/openapi.yaml")
async def openapi_spec():
    """
        注册用的：返回插件所依赖的插件服务的API接口描述，参照openapi规范编写。
        注意：API路由是固定的，事先约定的。
    """
    with open(".well-known/openapi.yaml", encoding="utf-8") as f:
        text = f.read()
        return text, 200, {"Content-Type": "text/yaml"}


@app.route("/.well-known/ui.json")
async def ui_spec():
    """
        注册用的：返回插件的描述文件，描述了插件是什么等信息。
        注意：API路由是固定的，事先约定的。
    """
    host = request.host_url
    with open(".well-known/ui.json", encoding="utf-8") as f:
        text = f.read()
        return text, 200, {"Content-Type": "application/json"}



@app.route('/')
def index():
    return 'welcome to my webpage!'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8081)