import requests

# URL and cookies
url = "https://www.butian.net/Reward/pub"
cookies = {
    "wzws_sessionid": "gDExNy4xNzYuMjE5LjIyM4ExMjBmMDagZnjYS4JiYTUyNDQ=",
    "PHPSESSID": "qqcrg07ik5jdl65euq87466n14",
    "__btu__": "1fe90b40e8df7e5e98f9765a38e5ad487cf85b0d",
    "__btc__": "5ab65f4a70eb5af16a2faea7908bc066242c3098",
    "__btuc__": "27d916aff517a60a769a2156b59c78dea92e7779"
}

# Headers
headers = {
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary84gHsdRpvpUfZBLY",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Sec-Ch-Ua-Platform": "\"Linux\"",
    "Origin": "https://www.butian.net",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.butian.net/Reward/plan/2",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=1, i",
    "Connection": "close"
}

# Function to send a single POST request
def send_post_request(company_name):
    boundary = "----WebKitFormBoundary84gHsdRpvpUfZBLY"
    multipart_data = (
        f"--{boundary}\r\n"
        "Content-Disposition: form-data; name=\"ajax\"\r\n\r\n"
        "1\r\n"
        f"--{boundary}\r\n"
        "Content-Disposition: form-data; name=\"name\"\r\n\r\n"
        f"{company_name}\r\n"
        f"--{boundary}\r\n"
        "Content-Disposition: form-data; name=\"p\"\r\n\r\n"
        "1\r\n"
        f"--{boundary}--\r\n"
    )
    multipart_data_bytes = multipart_data.encode('utf-8')
    response = requests.post(url, headers=headers, cookies=cookies, data=multipart_data_bytes)
    return response

# Read company names from a file and send POST requests
with open('company_names.txt', 'r', encoding='utf-8') as file:
    company_names = file.readlines()

for company_name in company_names:
    company_name = company_name.strip()
    if company_name:  # Skip empty lines
        response = send_post_request(company_name)
        print(f"Response for {company_name}: {response.status_code}")
        print(response.text)
