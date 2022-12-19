# import flask modules
from flask import Flask, send_from_directory

# import funcs/blueprints
from main.views import main_blueprint
from loader.views import loader_blueprint

# constants
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

# starting app
app = Flask(__name__)

# registering blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# configuring app
app.config['POST_PATH'] = POST_PATH


# setting path directory
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


# running app with debug mode
app.run(debug=True)
