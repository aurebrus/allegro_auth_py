import requests
import json

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = "http://localhost:5000/"
AUTH_URL = "https://allegro.pl/auth/oauth/authorize"
TOKEN_URL = "https://allegro.pl/auth/oauth/token"


def get_authorization_code():
    authorization_redirect_url = AUTH_URL + '?response_type=code&client_id=' + CLIENT_ID + \
                                 '&redirect_uri=' + REDIRECT_URI
    print("go to the following url on the browser and enter the code from the returned url: ")
    print("---  " + authorization_redirect_url + "  ---")
    authorization_code = input('code: ')
    return authorization_code


def get_access_token(authorization_code):
    try:
        data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': REDIRECT_URI}
        print("requesting access token")
        access_token_response = requests.post(TOKEN_URL, data=data, verify=False,
                                              allow_redirects=False, auth=(CLIENT_ID, CLIENT_SECRET))
        tokens = json.loads(access_token_response.text)
        access_token = tokens['access_token']
        return access_token
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def main():
    authorization_code = get_authorization_code()
    access_token = get_access_token(authorization_code)
    print("access token =" + access_token)


if __name__ == "__main__":
    main()
