import requests
import time


# remaining = r.headers["X-RateLimit-Remaining"]
# reset_time = r.headers["X-RateLimit-Reset"]

# current_time = time.time()
# reset_time = int(reset_time)
# remaining_time = reset_time - current_time
# print("Remaining time (seconds)", remaining_time)

# time.sleep(remaining_time)

# Count stars
count = 0

for i in range(1, 5):
        r = requests.get("https://api.github.com/users/emaadmanzoor/repos?page=" + str(i))
        if r.status_code != 200:
            break 
        dicts = r.json()
        for s in dicts:
            count = count + int(s['stargazers_count'])
print(count)

