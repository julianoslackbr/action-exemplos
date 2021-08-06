from flask import Flask, request
import os
import redis
#import flask_redis

import jsonify
import json

app = Flask(__name__)
#redis_db = redis.Redis.from_url("redis://localhost:6379/0")

redis_host = os.getenv("REDIS_HOST", default='localhost')
redis_db = redis.StrictRedis(host=redis_host, port=6379)



@app.route('/', methods=['GET'])
def main():
  a = []
  for i in os.environ.items():
    a.append(i)  

  return str(a)

@app.route('/health', methods=['GET'])
def health():
  
  return "oi"

@app.route('/add/', methods=['GET'])
def redis_add():
  #a = redis_db.set("oi")
  #return  redis_db
  value = redis_db.incr('counter', 1)
  return 'Visitor number: {}'.format(value)

@app.route('/query')
def query_example():
  # query string exemplo:
  # http://localhost:5000/query?cor=amarelo&formato=quadrado
  
  # com .get retorna None caso não existe na querystring
  cor = request.args.get('cor')
  formato = request.args.get('formato')
  # apenas com args retorna bad request
  #  formato = request.args['formato']


  return '''Query String formato: {0} <br>
            Query String cor: {1}'''.format(formato, cor)

@app.route('/json')
def json_example():
    return 'JSON Object Example'  

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000 )