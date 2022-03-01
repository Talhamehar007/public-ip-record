import datetime
import os
import requests
from time import sleep

os.chdir(f"{os.getenv('HOME')}/.scripts/Record IP/")

datetime_format = '%a %d-%b-%Y %l:%M:%S %p'


def main():
    os.system("touch ./ip")
    old_ip = open("./ip", "r+").read()
    new_ip = "0.0.0.0"
    print("Old IP is", old_ip)

    try:
        new_ip: str = requests.get('https://api.ipify.org').text
        print("New IP is", new_ip)
    except Exception as e:
        open("./Log.txt", "a+").write(f"{str(datetime.datetime.now().strftime(datetime_format))}\t\t{e}\n")
        print("Exception Occurred, Trying Again. Sleeping for 5 minutes.")
        sleep(60)
        main()
    finally:
        print("Reached Finally Section.")
        if old_ip != new_ip:
            print(new_ip, "is NOT Same as ", old_ip, "So Writing The File")
            open("./Record.txt", "a+").write(f"{new_ip}\t\t{str(datetime.datetime.now().strftime(datetime_format))}\n")
            open("./ip", "w+").write(new_ip)
            print("New IP Written to both files. ")
        else:
            print("Both IPs are Same.")
        print("Sleeping for 10 Minutes and restarting the loop")
        sleep(60 * 10)

        main()


if __name__ == "__main__":
    main()
