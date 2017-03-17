from . import util


def get_domain_access_token(domain_api_key, domain_api_secret):
    url = util.base_url + "domains/accesstokens?key={0}&domain_api_secret{1}".format(domain_api_key, domain_api_secret)
    return util.http_get(url)


def delete_domain_access_token(domain_api_key, domain_api_secret, domain_access_token):
    url = util.base_url + "domains/accesstokens?key={0}&domain_api_secret={1}&domain_access_token={2}".format(domain_api_key, domain_api_secret, domain_access_token)
    return util.http_delete(url)


def get_limited_domain_detail(domain_api_key, domain_api_secret, domain_access_token):
    url = util.base_url + "accounts/domains/details?key={0}&domain_api_secret={1}&domain_access_token={2}".format(domain_api_key, domain_api_secret, domain_access_token)
    return util.http_get(url)


def create_user_by_phone_number(domain_access_token, user_details):
    url = util.base_url + "domains/users/phone_number?key={0}".format(domain_access_token)
    return util.http_post_json(url, user_details)


def create_user_by_user_id(domain_access_token, user_details):
    url = util.base_url + "domains/users/user_id?key={0}".format(domain_access_token)
    return util.http_post_json(url, user_details)


def delete_user(user_api_key):
    url = util.base_url + "domains/users?key={0}".format(user_api_key)
    return util.http_delete(url)


def get_users(domain_access_token):
    url = util.base_url + "domains/users?key={0}".format(domain_access_token)
    return util.http_get(url)


def get_user_details(domain_access_token, user_access_token):
    url = util.base_url + "domains/users/details?key={0}&user_access_token={1}".format(domain_access_token, user_access_token)
    return util.http_get(url)
