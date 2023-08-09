# Backarr
This project aims to be a simple off site/remote backup tool for the *arr suit of tools. It will aim to make backups easy without the need for using additional backup software and keep it light. Aimed for those who may try the *arr suite of app on a variety of hosts.
## Radarr/Sonarr Backup Automation

### Overview

This project provides a Python script to automate the process of downloading backups from Radarr, Sonarr, and other similar applications that use the same API. It supports multiple instances and different authentication methods, making it a flexible and scalable solution for managing backups across various environments.
Features

Multiple Instances Support: Easily configure and manage backups for multiple Radarr/Sonarr instances.
Various Authentication Methods: Supports 'None', 'Basic (browser popup)', and 'Forms (login page)' authentication.
Configurable via INI File: All settings, including host URLs, API keys, usernames, and passwords, are configurable via a simple INI file.
Size Verification: Verifies the size of the downloaded file against the expected size reported by the server.
Extendable: Designed to work with other apps that use the same API, making it extendable to other use cases.

### Usage

Configuration: Edit the config.ini file to include the details of the instances you want to manage. You can define different sections for each instance or app.
Running the Script: Execute the script to download the latest backups for the configured instances. The script will iterate through the sections defined in the configuration file, downloading and verifying the backups for each section.

### Requirements

    Python 3.x
    requests library


Feel free to open issues or submit pull requests.
