import hashlib
import requests
import json

URL = "https://api.close.com/buildwithus/"
resp = requests.get(URL)
print(resp.text)

data = json.loads(resp.text)
print(data["traits"])
print(data["key"])

TRAITS = data["traits"]
KEY = data["key"].encode('utf-8')

i = 0
json_hashes = ""
for trait in TRAITS:
    m = hashlib.blake2b(trait.encode(), digest_size=64, key=KEY)
    trait_hash = m.hexdigest()
    if i == 0:
        json_hashes = "[\"" + trait_hash + "\",\n"
    elif i == len(TRAITS) - 1:
        json_hashes += "\"" + trait_hash + "\"]\n"
    else:
        json_hashes += "\"" + trait_hash + "\",\n"
    i += 1
    
print(json_hashes)
resp = requests.post(URL, json = json.loads(json_hashes))

print(resp.text)