import requests
import time
import datetime
import argparse
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[logging.FileHandler("ip_monitor.log"),
                              logging.StreamHandler()])

# Arguments parser
parser = argparse.ArgumentParser(description='Monitor Public IP address')
parser.add_argument('-i', '--interval', type=int, default=60, help='Interval in seconds')
parser.add_argument('-d', '--daemon', action='store_true', help='Run script as daemon')
parser.add_argument('-db', '--database', type=str, default='ip_logs.db', help='SQLite3 database file')
args = parser.parse_args()

# Connect to database
try:
    conn = sqlite3.connect(args.database, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ip_logs (ip TEXT, timestamp TIMESTAMP)''')
    conn.commit()
    logging.info("Connected to database %s", args.database)
except Exception as e:
    logging.error("Failed to connect to database %s", args.database, exc_info=e)
    exit(1)

previous_ip = None

# Read previous IP from database
try:
    cursor.execute("SELECT ip FROM ip_logs ORDER BY timestamp DESC LIMIT 1")
    previous_ip = cursor.fetchone()[0]
    logging.info("Previous IP: %s", previous_ip)
except Exception as e:
    logging.error("Failed to read previous IP from database", exc_info=e)

while True:
    try:
        # Fetch public IP
        public_ip = requests.get("https://api.ipify.org").text

        # Compare current IP with previous IP
        if public_ip != previous_ip:
            # Write current IP and timestamp to database
            cursor.execute("INSERT INTO ip_logs (ip, timestamp) VALUES (?, ?)", (public_ip, datetime.datetime.now()))
            conn.commit()
            logging.info("IP changed: %s", public_ip)

            # Update previous IP
            previous_ip = public_ip
    except Exception as e:
        logging.error("Error: %s", e, exc_info=e)

    if args.daemon:
        time.sleep(args.interval)
    else:
        break

# Close database connection
conn.close()
