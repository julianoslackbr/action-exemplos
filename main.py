from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
  a = []
  for i in os.environ.items():
    a.append(i)  

  return str(a)

if __name__ == '__main__':
  app.run(debug=True)