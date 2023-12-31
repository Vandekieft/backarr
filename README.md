# Backarr
## Radarr/Sonarr Backup Automation
### Overview

This project provides a Python script to automate the process of downloading backups from Radarr, Sonarr, and other similar applications that use the same API. It supports multiple instances and different authentication methods, making it a flexible and scalable solution for managing backups across various environments.
Features

- Multiple Instances Support:
    - Easily configure and manage backups for multiple Radarr/Sonarr instances.
- Various Authentication Methods:
    - Supports 'None', 'Basic (browser popup)', and 'Forms (login page)' authentication.
- Configurable via INI File:
    -  All settings, including host URLs, API keys, usernames, passwords, and download path, are configurable via a simple INI file.
- Size Verification:
    -  Verifies the size of the downloaded file against the expected size reported by the server.
- Extendable:
    -  Designed to work with other apps that use the same API, making it extendable to other use cases.

### Usage

Save the backarr.py and config.ini in the same directory
- Configuration:
    - Edit the config.ini file to include the details of the instances you want to manage. You can define different sections for each instance or app. 

config Example:
    
    [radarr_instance1]
    host = https://radarr1.example.com
    api_key = api_key_for_instance1
    username = username_for_instance1
    password = password_for_instance1
    auth_method = Forms
    download_path = ./downloads

Change the following line in backarr.py to reflect your ini:

   ` sections_to_process = ['radarr_instance1', 'radarr_instance2', 'sonarr_instance1']`

- Running the Script:
    - Execute the script to download the latest backups for the configured instances. The script will iterate through the sections defined in the configuration file, downloading and verifying the backups for each section.

From the directorty you have files saved:

   ` python backarr.py`

Requirements:

    Python 3.x
    requests library

- Notes:
    - Make sure to set the appropriate permissions on the config.ini file to restrict access to sensitive information. The download_path variable in the INI file specifies the directory where the backups will be downloaded. Make sure the directory exists and has the appropriate permissions.


Feel free to open issues or submit pull requests.
