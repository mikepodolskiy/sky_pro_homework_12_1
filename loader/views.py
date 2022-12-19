# import flask modules
from flask import Blueprint, render_template, request, current_app

# import functions
from loader.utils import save_upload_picture
from main.utils import PostsHandler
import logging

# creating blueprint, setting templates folder
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

# configuring logging
logging.basicConfig(filename='basic.log', level=logging.INFO)


# calling blueprint route, returning as required html template
@loader_blueprint.route('/post')
def create_new_post():
    return render_template('post_form.html')


# calling blueprint route for
@loader_blueprint.route('/post', methods=['POST'])
def create_new_post_from_user_data_page():
    """
    blueprint for uploading post
    :return: uploaded post in required template
    """

    # getting picture that was sent from input
    picture = request.files.get('picture')
    # getting content from form
    content = request.form.get('content')

    # checking if data is correct
    if not picture or not content:
        logging.basicConfig(filename='error.log', level=logging.ERROR)
        return 'Data failed'

    # checking if picture was correct
    picture_path = save_upload_picture(picture)

    # logging if wrong file type
    if not picture_path:
        logging.info(f'File: {picture.filename} is not a picture')
        return 'Wrong file format'

    # logging if error of uploaded data - key/value
    posts_handler = PostsHandler(current_app.config['POST_PATH'])
    new_post = {'pic': picture_path, 'content': content}
    error = posts_handler.add_post(new_post)
    if error:
        logging.error(f'Post uploading error: {error}')
        return 'Upload error'

    return render_template('post_uploaded.html', picture_path=picture_path, content=content)
