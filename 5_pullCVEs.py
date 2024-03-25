import requests
import json

def main():
    content = requests.get("http://cve.circl.lu/api/last")
    jsonfile = content.json()
    print(jsonfile)
    for item in jsonfile:
        print(f"ID: {item['id']}, SUMMARY: {item['summary']}")

if __name__== "__main__":
    main()

