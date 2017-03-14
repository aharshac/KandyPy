# **Kandy**
A Python REST API wrapper for Kandy.io


## **Account**
An account is automatically created for you when you register on the Kandy portal. An account has an API key and API secret, that are visible at the My Kandy section ("My Projects" tab) of the portal once you are logged in.

The API key and API secret can be used to create an account access token, which is then used in API calls to perform activities that require account level privileges.

These actions include:
* Domain management
* Account authentication management

```
IMPORT:
from Kandy import Account
```


### Get Account Access Token
Get access token for an account (server side).  

```
FUNCTION:
get_account_access_token(api_key, api_secret)

ARGS:
api_key = API key of Account (string, required)
api_secret = API secret of Account  (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "success",
  "result": {
    "account_access_token": "AATXX"
  }
}
```

### Delete Account Access Token
Delete account access token (server side).

```
FUNCTION:
delete_account_access_token(api_key, account_api_secret, account_access_token)

ARGS:
api_key = API key of Account (string, required)
api_secret = API secret of Account (string, required)
account_access_token = Access token to be revoked	(string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "success"
}
```

### Create Domain
```
FUNCTION:
create_domain(account_access_token, domain_name, project_name)

ARGS:
account_access_token = Access token of account (string, required)
domain_name = Name of domain (string, required)
project_name = Human readable description of domain (string, optional)

RETURN: (JSON)
{
  "domain_name": "test.com",
  "project_name": "test domain for my account"
}
```

### Delete Domain
```
FUNCTION:
delete_domain(account_access_token, domain_api_key)

ARGS:
account_access_token = Access token of account (string, required)
domain_api_key = API key of Domain (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "Domain Deleted"
}
```

### Get List of Domains
```
FUNCTION:
get_domains(account_access_token)

ARGS:
account_access_token = Access token of account (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "success",
  "result": {
    "domains": [
      {
        "domain_api_key": "668a9a133f85d80a9c84e2772a82aa59",
        "domain_api_secret": "95aa28a2772e48c9a08d58f331a9a866",
        "domain_name": "domain.com",
        "project_name": "my domain",
        "account_number": "00000012",
        "account_email": "owner@domain.com",
        "number_of_users": "41",
        "next_recurring_payment": "2015-01-19"
      }
    ]
  }
}
```
