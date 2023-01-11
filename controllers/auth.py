def controller_endpoints(app):
    @app.route('/', methods=['GET'])
    def home():
        print("Entrando")
        return "Hola"
