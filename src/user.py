from Kandy.src import util

class User:
    def get_user_access_token(self, domain_api_key, domain_api_secret, user_id):
        url = util.base_url + "domains/users/accesstokens?key={0}&domain_api_secret={1}&user_id={2}".format(domain_api_key, domain_api_secret, user_id)
        return util.http_get(url)
        
    def create_device(self, user_access_token, device_details):
        url = util.base_url + "users/devices?key={0}".format(user_access_token)
        return util.http_post_json(url, device_details)  
        
    def delete_device(self, user_access_token, device_id):
        url = util.base_url + "users/devices?key={0}&device_id={1}".format(user_access_token, device_id)
        return util.http_delete(url)
        
    def get_devices(self, user_access_token):
        url = util.base_url + "users/devices?key={0}".format(user_access_token)
        return util.http_get(url)