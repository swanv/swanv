from flask import jsonify
from app.api import bp

@bp.route('/ping', methods = ['GET'])
def ping():
    '''前端 vue.js 用来测试与后端的 Flask API 的连通性'''
    return jsonify('Pong!')