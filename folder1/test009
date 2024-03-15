# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:49:52 2024


"""

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.runtime.client_runtime_context import RequestOptions
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
import json
#pip install Office365-REST-Python-Client

username = 'Nelvin.Moonesawmy@mu.ey.com'
print("Input password for " + username)
password = input()
site_url = 'https://sites.ey.com/sites/GroupamaSACKT'
list_title = 'Shared Documents/General'
file_name = 'datatest2.xlsx'
api_url = f'{site_url}/_api/web/GetFolderByServerRelativeUrl(\'{list_title}\')/Files'

credential_options = {
  'username': username,
  'password': password,
}

# Authentication
ctx_auth = AuthenticationContext(site_url)
if ctx_auth.acquire_token_for_user(credential_options['username'], credential_options['password']):
  ctx = ClientContext(site_url, ctx_auth)
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print('Authenticated into SharePoint:', web.properties['Title'])
else:
  print(ctx_auth.get_last_error())

# Function for extracting file names from a folder in SharePoint
def print_folder_contents(ctx):
  try:
    request = RequestOptions((api_url))
    response = ctx.pending_request().execute_request_direct(request)
    jsonlist = json.loads(response.content)
    return jsonlist
  except Exception as e:
    print('Problem printing out library contents:', e)

# Function for downloading file 
def download_files(ctx):
  print("Enter File name you wish to download:")
  file_name= input().strip()
  file_url = f'{site_url}/_api/web/GetFolderByServerRelativeUrl(\'{list_title}\')/Files(\'{file_name}\')/$value'

  try:
    request = RequestOptions((file_url))
    response = ctx.pending_request().execute_request_direct(request)
    with open(f"./{file_name}", "wb") as local_file:
      local_file.write(response.content)
    print("file downloaded")
  except Exception as e:
    print('Problem getting file:', e)




res = print_folder_contents(ctx)
print("List of files available:")
for files_name in res['d']['results']:
    print(files_name['Name'])

download_files(ctx)
