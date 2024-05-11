from flask import Flask

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config['SECRET_KEY'] = 'your_unique_and_secret_key_here'


from app.controller.controller_index import *
if __name__ == '__main__':
    app.run(debug=True)
