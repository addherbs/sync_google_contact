import httplib2
import os
import argparse

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/people.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/contacts'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'People API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('./')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'people.googleapis.com-python-saved_credentials.json')

    store = Storage(credential_path)
    cred = store.get()
    if not cred or cred.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            cred = tools.run_flow(flow, store, flags)

        print('Storing credentials to ' + credential_path)
    return cred


def create_contact(name, phone, email='None'):
    service.people().createContact(body={
        "names": [
            {"givenName": name}
        ],
        "phoneNumbers": [
            {'value': phone}
        ],
        "emailAddresses": [
            {'value': email}
        ]
    }).execute()


credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('people', 'v1', http=http,
                          discoveryServiceUrl='https://people.googleapis.com/$discovery/rest')

# try:
#     create_contact("lol", "123", "lol@lol.com")
# except discovery.HttpError as exception:
#     print("raise HttpError")
create_contact("lol", "123", "lol@lol.com")
