from flask import Flask, request, jsonify
import json 

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
   
    # Retorna um objeto JSON como resposta
    data={'item':[{'nome':'ola'}]}
    jsonss = json.dumps(data)
    return jsonss

if __name__ == '__main__':
    app.run(debug=True)