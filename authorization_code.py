import requests
import json

CLIENT_ID = '42c06fb738594d198e571b47d39bdd75'
CLIENT_SECRET = 'ifPKW8LZUNfEKEIhvDaOcMzP4daIhQEcmE7qB9iQMRlxdQKLxBhncLIrUp2piGyC'
REDIRECT_URI = "http://localhost:5000/"
AUTH_URL = "https://allegro.pl/auth/oauth/authorize"
TOKEN_URL = "https://allegro.pl/auth/oauth/token"


def get_authorization_code():
    authorization_redirect_url = AUTH_URL + '?response_type=code&client_id=' + CLIENT_ID + \
                                 '&redirect_uri=' + REDIRECT_URI
    print("Login to Allegro - use url in your browser and then enter authorization code from returned url: ")
    print("---  " + authorization_redirect_url + "  ---")
    authorization_code = input('code: ')
    return authorization_code


def get_access_token(authorization_code):
    try:
        data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': REDIRECT_URI}
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
    print("access token = " + access_token)


if __name__ == "__main__":
    main()
