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
page_num = 1

while True:
        r = requests.get("https://api.github.com/users/emaadmanzoor/repos?page_num=" + str(page_num))
        if. r.status_code !=200:
        break
       
        Data = r.json()
        for repo in Data:
            count = count + int(repo['stargazers_count'])
        page_num = page_num + 1
print(count)

