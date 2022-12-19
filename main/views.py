# import flask modules
from flask import Blueprint, render_template, request, current_app

# import functions
from main.utils import PostsHandler
import logging

# creating blueprint, setting template folder
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
# configuring logging, considering encoding
logging.basicConfig(handlers=[logging.FileHandler(filename='basic.log', encoding='utf-8', mode='a+')],
                    level=logging.INFO)


# calling blueprint for main page in required template
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


# calling blueprint for search page
@main_blueprint.route('/search')
def search_page():
    """
    returns search results as a list of posts in required template
    :return:
    """
    # getting data from address bar as 's'
    string = request.args.get('s', '')
    # writing to log file
    logging.info(f'Search for: {string}')
    # configuring app
    posts_handler = PostsHandler(current_app.config['POST_PATH'])
    # getting list of posts with required word with search_posts method
    posts = posts_handler.search_posts(string)

    return render_template('post_list.html', posts=posts, string=string)
