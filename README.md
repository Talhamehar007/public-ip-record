# IP Monitor

IP Monitor is a simple Python script that monitors the public IP address of your computer and writes the unique IP addresses and timestamps to an SQLite3 database. The script can also be run as a daemon, it will keep running in the background and check the IP address at a specified interval.

## Features

- Fetch public IP of your computer
- Compare the current IP with the previous IP and write unique values to a SQLite3 database with date stamps
- Option to run script as daemon, with a specified interval
- Logging to a file and console
- Command-line arguments

## Usage

1. Install Python3 and the `requests` library
2. Download the script and place it in a folder
3. Open the terminal and navigate to the folder
4. Run the script by executing:

   **`python3 ip-logger.py`**

5. You can also use the following command-line arguments to configure the script:
   -i, --interval Interval in seconds (default: 60)
   -d, --daemon Run script as daemon
   -db, --database SQLite3 database file (default: ip_logs.db)

## Adding to startup

The script can be added to start on startup on Linux, you can use the following methods:

1. **systemd service**: You can create a systemd service and configure it to start on boot. This method is recommended if you want to run the script as a daemon.
2. **cron job**: You can create a cron job that runs the script at startup or at a specified interval.

## How this can be improved

- Email notifications: You can add a feature that sends an email notification when the public IP changes.
- Logging to a remote server: Instead of logging to a local file, you can log to a remote server.
- More options for the database: Instead of SQLite3 you can use other databases like MySQL, PostgreSQL, etc.

## What's the use case

- Dynamic IP addresses: If your internet service provider assigns you a dynamic IP address, it can change frequently. This script can help you keep track of IP address changes.
- Remote access: If you need to remotely access your computer, you need to know its IP address. This script can help you keep track of the current IP address.

## Future TODO

- Add email notifications
- Add support for remote logging
- Add support for different databases

## Contribution

If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

Please note that this script is for educational purposes, and it is recommended to use a more robust and secure solution to monitor your IP address if you need it in production.
