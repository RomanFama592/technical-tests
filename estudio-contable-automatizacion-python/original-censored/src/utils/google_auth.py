from env import scope, creds_file, client_oauth
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from src.utils.json_to_dict import json_to_dict
from oauth2client.client import OAuth2WebServerFlow, OAuth2Credentials


def oauth() -> OAuth2Credentials:
    try:
        with open(creds_file) as file_creds:
            creds = OAuth2Credentials.from_json(file_creds.read())
        if not creds.access_token_expired:
            return creds
        else:
            raise Exception()
    except:
        client = json_to_dict(client_oauth)["web"]

        server = OAuth2WebServerFlow(
            client["client_id"],
            client["client_secret"],
            scope=scope,
            redirect_uri=client["redirect_uris"],
        )

        return run_flow(server, Storage(creds_file))
