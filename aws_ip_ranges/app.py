import requests

def main():
    ip_ranges = fetch_ip_ranges()
    prefixes = ip_ranges["prefixes"]
    print(type(prefixes))

    services = set()

    for prefix in prefixes:
        services.add(prefix["service"])
    
    print(services)

def fetch_ip_ranges():
    res = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json")
    return res.json()

if __name__ == "__main__":
    exit(main())
