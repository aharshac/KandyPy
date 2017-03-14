from Kandy.src import util

class Device:
    def get_device_address_book(self, user_access_token, device_id):
        url = util.base_url + "devices/addressbooks?key={0}&device_id={1}".format(user_access_token, device_id)
        return util.http_get(url)

    def delete_device_address_book(self, user_access_token, device_id):
        url = util.base_url + "devices/addressbooks?key={0}&device_id={1}".format(user_access_token, device_id)
        return util.http_delete(url)
        
    def send_message(self, user_access_token, device_id, message):
        url = util.base_url + "devices/messages?key={0}&device_id={1}".format(user_access_token, device_id)
        return util.http_post_json(url, message)
        
    def get_pending_messages(self, user_access_token, device_id, client_timestamp):
        url = util.base_url + "devices/messages?key={0}&device_id={1}&client_timestamp={2}".format(user_access_token, device_id, client_timestamp)
        return util.http_get(url)
        
    def delete_handled_messages(self, user_access_token, device_id, messages):
        url = util.base_url + "devices/messages?key={0}&device_id={1}&messages={2}".format(user_access_token, device_id, messages)
        return util.http_delete(url)