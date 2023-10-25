import requests
from lib.utils import build_request_headers
from config import SESSION, LOG

class Users:

    def __init__(self):
        self.users_url= "/users"

    def get_all_users(self, app_url, access_token):
        LOG.info("get_all_users")
        request_headers = build_request_headers(access_token)
        response = SESSION

    def create_user(self, app_url, access_token, username, password, role="user"):


    def get_current_user(self, app_url, access_token):

    def delete_user(self, app_url, access_token, user_id):


