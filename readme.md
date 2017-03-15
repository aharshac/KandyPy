# **Kandy**
A Python REST API wrapper for Kandy.io

&nbsp;

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

&nbsp;

## **Domain** (Project)

A domain is a collection of users that form a community (i.e. they can interact with each other through Kandy calls and messages). Once you have an account, you can create domains.

A domain has an API key and API secret, that are visible at the My Kandy section ("My Projects" tab) of the portal once you are logged in.

The API key and API secret can be used to create a domain access token, which is then used in API calls to perform activities that require domain level privileges to do.

These actions include:
* User management
* Hunt group management
* Various general services

```
IMPORT:
from Kandy import Domain
```


### Get Domain Access Token
Get access token for a domain

```
FUNCTION:
get_domain_access_token(domain_api_key, domain_api_secret)

ARGS:
domain_api_key = API key of Domain (string, required)
domain_api_secret = API secret of Domain  (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "success",
  "result": {
    "domain_access_token": "4d405f6dfd9842a981a90daaf0da08fa"
  }
}
```

### Delete Domain Access Token
Revoke access token for a domain

```
FUNCTION:
delete_domain_access_token(domain_api_key, domain_api_secret, domain_access_token)

ARGS:
domain_api_key = API key of Domain (string, required)
domain_api_secret = API secret of Domain  (string, required)
domain_access_token = Access token of Domain (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "success"
}
```

### Limited Domain Detail
Get limited details of a domain by domain access token
Validates the existence of a provided domain key.

```
FUNCTION:
get_limited_domain_detail(domain_api_key, domain_api_secret, domain_access_token)

ARGS:
domain_api_key = API key of Domain (string, required)
domain_api_secret = API secret of Domain  (string, required)
domain_access_token = Access token of Domain (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "success",
  "result": {
    "domain": {
      "domain_api_key": "668a9a133f85d80a9c84e2772a82aa59",
      "domain_api_secret": "95aa28a2772e48c9a08d58f331a9a866",
      "domain_name": "domain.com",
      "project_name": "my domain",
      "account_number": "00000012",
      "account_email": "owner@domain.com",
      "number_of_users": "41",
      "next_recurring_payment": "2015-01-19"
    }
  }
}
```

### Create user by Phone Number
Refer [Kandy docs](https://developer.kandy.io/docs/rest-api#domain-create-user-by-phone-number) for additional info.

```
FUNCTION:
create_user_by_phone_number(domain_access_token, user_details)

ARGS:
domain_access_token = Access token of Domain (string, required)
user_details = Details of User (JSON, required)

TYPICAL user_details:
{
  "user_phone_number": "3524096582",
  "user_country_code": "US"
}

RETURN: (JSON)
{
  "status": 0,
  "message": "success"
}
```

### Create user by User ID
Refer [Kandy docs](https://developer.kandy.io/docs/rest-api#domain-create-user-by-userid) for additional info.

```
FUNCTION:
 create_user_by_user_id(domain_access_token, user_details):

ARGS:
domain_access_token = Access token of Domain (string, required)
user_details = Details of User (JSON, required)

TYPICAL user_details:
{
  "user_id": "russ",
  "user_country_code": "US"
}

RETURN: (JSON)
{
  "status": 0,
  "message": "success"
}
```

### Delete User
```
FUNCTION:
delete_user(user_api_key)

ARGS:
user_api_key = API key of User (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "User Deleted"
}
```

### Get List of Users
Returns listing of known Kandy users for domain
```
FUNCTION:
get_users(domain_access_token)

ARGS:
domain_access_token = Access token of Domain (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "success",
  "result": {
    "users": [
      {
        "user_api_key": "4d405f6dfd9842a981a90daaf0da08fa",
        "user_api_secret": "c6f9c881b6b64c2389d5b45d65a9dfd0",
        "user_id": "13524096582",
        "domain_name": "domain.com",
        "user_phone_number": "3524096582",
        "user_country_code": "1"
      }
    ]
  }
}
```

### Get User Details
Get full details of a user.
```
FUNCTION:
get_user_details(domain_access_token, user_access_token)

ARGS:
domain_access_token = Access token of Domain (string, required)
user_access_token = Access token of User (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "success",
  "result": {
    "users": [
      {
        "user_api_key": "4d405f6dfd9842a981a90daaf0da08fa",
        "user_api_secret": "c6f9c881b6b64c2389d5b45d65a9dfd0",
        "user_id": "13524096582",
        "domain_name": "domain.com",
        "user_phone_number": "3524096582",
        "user_country_code": "1"
      }
    ]
  }
}
```


&nbsp;

## **User**

```
IMPORT:
from Kandy import User
```

### Get User Access Token
Get access token for a User
This server side API provides an account access token after securely sending the API secret of the account.
```
FUNCTION:
get_user_access_token(domain_api_key, domain_api_secret, user_id)

ARGS:
domain_api_key = API key of Domain (string, required)
domain_api_secret = API secret of Domain (string, required)
user_id	= ID of User (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "success",
  "result": {
    "user_access_token": "4d405f6dfd9842a981a90daaf0da08fa"
  }
}
```

### Create Device
This will create/establish a new device to the user.
Refer [Kandy docs](https://developer.kandy.io/docs/rest-api#user-create-device) for additional info.
```
FUNCTION:
create_device(user_access_token, device_details)

ARGS:
user_access_token = Access token of User (string, required)
device_details = Details of Device (JSON, required)

TYPICAL device_details:
{
  "device_native_id": "12345678901234",
  "device_family": "iphone",
  "device_name": "iphone6",
  "client_sw_version": "0102001",
  "device_os_version": "8.0"
}

RETURN: (JSON)
{
  "status": 0,
  "message": "success",
  "result": {
    "device_id": "4d405f6dfd9842a981a90daaf0da08fa"
  }
}
```

### Delete Device
Delete an existing domain user
```
FUNCTION:
delete_device(user_access_token, device_id)

ARGS:
user_access_token = Access token of User (string, required)
device_id = Device ID of the device to be deleted (JSON, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "Device Deleted"
}
```

### Get List of Devices
Retrieve list of all user devices
```
FUNCTION:
get_devices(self, user_access_token)

ARGS:
user_access_token = Access token of User (string, required)

RETURN: (JSON)
{
  "status": 0,
  "message": "success",
  "result": {
    "devices": [
      {
        "device_id": "4d405f6dfd9842a981a90daaf0da08fa",
        "device_native_id": "12345678901234",
        "device_family": "iphone",
        "device_name": "iphone6",
        "client_sw_version": "0102001",
        "device_os_version": "8.0"
      }
    ]
  }
}
```
