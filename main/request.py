import requests
import random

# List of User-Agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/86.0"
]

# List of Proxies
proxies = [
    {"http": "http://proxy1:port", "https": "http://proxy1:port"},
    {"http": "http://proxy2:port", "https": "http://proxy2:port"}
]

# URL of the website
url = "https://yourwebsite.com"

# Simulate visits
for i in range(10):  # Adjust range for more visits
    headers = {"User-Agent": random.choice(user_agents)}
    proxy = random.choice(proxies)
    response = requests.get(url, headers=headers, proxies=proxy)
    print(f"Visit {i+1}: Status Code {response.status_code}")
