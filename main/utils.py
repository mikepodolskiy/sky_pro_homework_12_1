# import libraries
import json


# definition PostsHandler class to use its methods in other files
class PostsHandler:
    def __init__(self, path):
        self.path = path

    def load_posts_from_json(self):
        """
        open data from json file
        :return: data with posts
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def search_posts(self, string):
        """
        searching for required word in content of posts
        :param string: word for search
        :return: list of posts, contains word
        """
        posts = []
        for post in self.load_posts_from_json():
            if string.lower() in post['content'].lower():
                posts.append(post)

        return posts

    def save_posts_to_json(self, posts):
        """
        add to json file with all posts, catching error
        :param posts: file
        :return: error if occurred
        """
        try:
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(posts, file)
        except Exception as e:
            return e

    def add_post(self, post):
        """
        adds new post to post list
        :param post: new post
        """
        posts = self.load_posts_from_json()
        posts.append(post)
        self.save_posts_to_json(posts)
