import hashlib
import requests
import json

URL = "https://api.close.com/buildwithus/"
resp = requests.get(URL)
print(resp.text)

data = json.loads(resp.text)
TRAITS = data["traits"]
KEY = data["key"].encode('utf-8')

print(f"TRAITS: {TRAITS}")
print(f"KEY: {KEY}")

a_hashes = [] #""
for trait in TRAITS:
    m = hashlib.blake2b(trait.encode(), digest_size=64, key=KEY)
    trait_hash = m.hexdigest()
    a_hashes += [f"{trait_hash.encode('utf-8').decode()}"]

json_hashes = json.dumps(a_hashes)
print(f"JSON HASHES:\n{json_hashes}")

resp = requests.post(URL, json = json.loads(json_hashes))

print(resp.text)
