from . import util


def get_device_address_book(user_access_token, device_id):
    url = util.base_url + "devices/addressbooks?key={0}&device_id={1}".format(user_access_token, device_id)
    return util.http_get(url)


def delete_device_address_book(user_access_token, device_id):
    url = util.base_url + "devices/addressbooks?key={0}&device_id={1}".format(user_access_token, device_id)
    return util.http_delete(url)


def send_message(user_access_token, device_id, message):
    url = util.base_url + "devices/messages?key={0}&device_id={1}".format(user_access_token, device_id)
    return util.http_post_json(url, message)


def send_sms(user_access_token, device_id, source, destination, text):
    url = util.base_url + "devices/smss?key={0}&device_id={1}".format(user_access_token, device_id)
    payload = {
        "message": {
            "source": source,
            "destination": destination,
            "message": {
                "text": text
            }
        }
    }
    return util.http_post_json(url, payload)


def get_pending_messages(user_access_token, device_id, client_timestamp):
    url = util.base_url + "devices/messages?key={0}&device_id={1}&client_timestamp={2}".format(user_access_token, device_id, client_timestamp)
    return util.http_get(url)


def delete_handled_messages(user_access_token, device_id, messages):
    url = util.base_url + "devices/messages?key={0}&device_id={1}&messages={2}".format(user_access_token, device_id, messages)
    return util.http_delete(url)
