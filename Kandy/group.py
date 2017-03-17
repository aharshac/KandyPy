from . import util

class Group:
    def get_group_by_id(self, user_access_token, group_id):
        url = util.base_url + "users/chatgroups/chatgroup?key={0}&group_id={1}".format(user_access_token, group_id)
        return util.http_get(url)

    def send_message(self, user_access_token, message):
        url = util.base_url + "users/chatgroups/chatgroup/messages?key={0}".format(user_access_token)
        return util.http_post_json(url, message)
