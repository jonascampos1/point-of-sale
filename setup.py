from flask import Flask
import psycopg2

msg=""
try:
    conn= psycopg2.connect(
        host='db',
        user='jonas',
        password='password',
        port='5432'
    )
    print("===================Conexion exitosa")
    msg="Conexion Exitosa"
except Exception as ex:
    msg = f"Error Connection DB: {ex}"
    print(ex)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    print("Entrando")
    return msg


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)