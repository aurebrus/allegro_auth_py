import requests
import json

CLIENT_ID = ''          # enter the Client_ID of the application
CLIENT_SECRET = ''      # enter Client_Secret
TOKEN_URL = "https://allegro.pl/auth/oauth/token"


def get_access_token():
    try:
        data = {'grant_type': 'client_credentials'}
        access_token_response = requests.post(TOKEN_URL, data=data, verify=False, allow_redirects=False, auth=(CLIENT_ID, CLIENT_SECRET))
        tokens = json.loads(access_token_response.text)
        access_token = tokens['access_token']
        return access_token
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def main():
    access_token = get_access_token()
    print("access token = " + access_token)


if __name__ == "__main__":
    main()

