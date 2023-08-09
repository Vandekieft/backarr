import configparser
import requests
import os

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# List of sections to process
sections_to_process = ['radarr_instance1', 'radarr_instance2', 'sonarr_instance1']

# Iterate over the sections to process
for section in sections_to_process:
    # Get the values from the current section
    host = config[section]['host']
    api_key = config[section]['api_key']
    username = config[section]['username']
    password = config[section]['password']
    auth_method = config[section]['auth_method']

# Authentication method: 'None', 'Basic', or 'Forms'
#auth_method = "Basic"

# URL for the backups
backup_url = f"{host}/api/v3/system/backup?apiKey={api_key}"

# Start a session
session = requests.Session()

## Errors:
status401 = "status code 401. Please check your API key and login method."

# Handle authentication
if auth_method == 'Basic':
    session.auth = (username, password)
elif auth_method == 'Forms':
    # URL for the login form
    login_url = f"{host}/login"
    login_data = {'username': username, 'password': password}
    login_response = session.post(login_url, data=login_data)
    if login_response.status_code == 401:
        print(f"Login failed with ",status401)
        exit()
    elif login_response.status_code != 200:
        print(f"Login failed with status code {login_response.status_code}")
        exit()

# Get the backups
response = session.get(backup_url)

if response.status_code == 200:
    backups = response.json()

    # Get the latest backup
    latest_backup = max(backups, key=lambda x: x['time'])

    # Download the latest backup
    download_url = f"{host}{latest_backup['path']}"
    download_response = session.get(download_url, stream=True)

    if download_response.status_code == 200:
        local_file_path = os.path.join("./", latest_backup['name'])
        with open(local_file_path, 'wb') as f:
            for chunk in download_response.iter_content(chunk_size=8192):
                f.write(chunk)

        # Verify the size of the downloaded file
        downloaded_size = os.path.getsize(local_file_path)
        if downloaded_size == latest_backup['size']:
            print(f"Downloaded {latest_backup['name']} successfully")
        else:
            print(f"Size mismatch for {latest_backup['name']}: expected {latest_backup['size']}, got {downloaded_size}")
    elif download_response.status_code == 401:
        print(f"Failed to download backup with ",status401)
    else:
        print(f"Failed to download backup {latest_backup['name']} with status code {download_response.status_code}")
elif response.status_code == 401:
        print(f"Failed to download backup with ",status401)
else:
    print(f"Request failed with status code {response.status_code}")