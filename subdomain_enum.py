import requests
import logging
import json
import datetime
import re

def setup_logger(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=level
    )

def validate_domain(domain):
    """
    Validate that the domain is a valid hostname (no http/https).
    """
    pattern = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    if re.match(pattern, domain):
        return True
    else:
        logging.error("Invalid domain format. Please enter a valid domain (e.g., example.com).")
        return False

def query_crtsh(domain):
    url = f'https://crt.sh/?q=%25.{domain}&output=json'
    logging.info(f"[*] Querying crt.sh for {domain}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            logging.error("Failed to fetch data from crt.sh")
            return []
        data = json.loads(response.text)
        subdomains = set()
        for entry in data:
            subdomain = entry['name_value']
            if '\n' in subdomain:
                subdomains.update(subdomain.split('\n'))
            else:
                subdomains.add(subdomain)
        return list(subdomains)
    except Exception as e:
        logging.error(f"Error querying crt.sh: {e}")
        return []

def query_otx(domain, api_key):
    logging.info(f"[*] Querying AlienVault OTX for {domain}")
    headers = {'X-OTX-API-KEY': api_key}
    url = f'https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns'
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            logging.error("Failed to fetch data from AlienVault OTX")
            return []
        data = response.json()
        subdomains = set()
        for record in data.get('passive_dns', []):
            hostname = record.get('hostname')
            if hostname and domain in hostname:
                subdomains.add(hostname)
        return list(subdomains)
    except Exception as e:
        logging.error(f"Error querying OTX: {e}")
        return []

def save_report(domain, subdomains):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"{domain}_subdomains_report.txt"
    try:
        with open(filename, "w") as f:
            f.write(f"# Subdomain Enumeration Report for {domain}\n")
            f.write(f"# Generated on: {timestamp}\n\n")
            for sub in sorted(subdomains):
                f.write(sub + "\n")
        logging.info(f"[+] Report saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving report: {e}")

def enumerate_subdomains(domain, otx_api_key=None, verbose=False):
    setup_logger(verbose)

    if not validate_domain(domain):
        logging.error("Domain validation failed. Exiting enumeration.")
        return []

    all_subdomains = set()

    # Query crt.sh
    subdomains_crtsh = query_crtsh(domain)
    logging.info(f"[+] Found {len(subdomains_crtsh)} subdomains from crt.sh")
    all_subdomains.update(subdomains_crtsh)

    # Query AlienVault OTX if API key is provided
    if otx_api_key:
        subdomains_otx = query_otx(domain, otx_api_key)
        logging.info(f"[+] Found {len(subdomains_otx)} subdomains from AlienVault OTX")
        all_subdomains.update(subdomains_otx)

    save_report(domain, all_subdomains)
    return sorted(all_subdomains)