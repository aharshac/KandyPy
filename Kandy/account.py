from . import util


def get_account_access_token(api_key, account_api_secret):
    url = util.base_url + "accounts/accesstokens?key={0}&account_api_secret={1}".format(api_key, account_api_secret)
    return util.http_get(url)


def delete_account_access_token(api_key, account_api_secret, account_access_token):
    url = util.base_url + "accounts/accesstokens?key={0}&account_api_secret={1}&account_access_token={2}".format(api_key, account_api_secret, account_access_token)
    return util.http_delete(url)


def create_domain(account_access_token, domain_name, project_name):
    url = util.base_url + "accounts/domains?key={0}".format(account_access_token)
    payload = {
        "domain_name": domain_name,
        "project_name": project_name
    }
    return util.http_post_json(url, payload)


def delete_domain(account_access_token, domain_api_key):
    url = util.base_url + "accounts/domains?key={0}&domain_api_key={1}".format(account_access_token, domain_api_key)
    return util.http_delete(url)


def get_domains(account_access_token):
    url = util.base_url + "accounts/domains?key={0}".format(account_access_token)
    return util.http_get(url)
