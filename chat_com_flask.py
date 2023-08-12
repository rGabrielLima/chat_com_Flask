from flask import Flask, render_template
from flask_socketio import SocketIO, emit

servidor = Flask(__name__, static_folder='static')
servidor.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(servidor)

#definindo as rotas e eventos docketIO
@servidor.route("/")
def index():
    return render_template("index.html")

@socketio.on("mensagem")
def handle_message(mensagem):
    emit("mensagem", mensagem, broadcast = True)

if __name__ == "__main__":
    socketio.run(servidor)