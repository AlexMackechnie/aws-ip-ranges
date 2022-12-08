import requests
import click

def main():
    response = fetch_ip_ranges()

    prefixes = response["prefixes"]

    services = set()

    # Get list of services
    for prefix in prefixes:
        services.add(prefix["service"])
    print(services)

    get_service_name(services)

@click.command()
@click.option('--service', type=click.Choice(['MD5', 'SHA1']))
def get_service_name(service):
    click.echo(service)


def fetch_ip_ranges():
    res = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json")
    return res.json()

def build_dict_keyed_by_service(ip_ranges):
    d = {}
    return d

if __name__ == "__main__":
    exit(main())
