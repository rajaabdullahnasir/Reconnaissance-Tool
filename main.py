import logging
from dns_enum import get_dns_records
from banner_grabber import grab_banner
from tech_detect import detect_with_wappalyzer
from subdomain_enum import enumerate_subdomains  
from whois_lookup import get_whois_info, print_whois_info

def main():
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    # Get user input
    domain = input("Enter domain (e.g., google.com): ").strip()
    url = f"https://{domain}"
    ports = [80, 443, 21, 22, 8080]

    # Ask if user wants to run subdomain enumeration
    run_subdomain_enum = input("Do you want to perform subdomain enumeration? (y/n): ").strip().lower() == "y"
    otx_api_key = None
    if run_subdomain_enum:
        use_otx = input("Do you want to use AlienVault OTX (requires API key)? (y/n): ").strip().lower() == "y"
        if use_otx:
            otx_api_key = input("Enter your AlienVault OTX API Key: ").strip()

        # SUBDOMAIN ENUMERATION
        print("\n====== SUBDOMAIN ENUMERATION RESULTS ======\n")
        try:
            subdomains = enumerate_subdomains(domain, otx_api_key=otx_api_key, verbose=True)
            if subdomains:
                print(f"\nTotal Subdomains Found: {len(subdomains)}\n")
                for sub in subdomains:
                    print(f"- {sub}")
            else:
                print("No subdomains found.")
        except Exception as e:
            print(f"Error in Subdomain Enumeration: {e}")

    # WHOIS LOOKUP
    run_whois = input("Do you want to perform WHOIS Lookup? (y/n): ").strip().lower() == "y"
    if run_whois:
        print("\n====== WHOIS LOOKUP ======\n")
        try:
            whois_data = get_whois_info(domain, verbose=True)
            if whois_data:
                print_whois_info(whois_data)
            else:
                print("WHOIS data not found.")
        except Exception as e:
            print(f"Error in WHOIS Lookup: {e}")
    
    # DNS ENUMERATION
    print("\n====== DNS ENUMERATION RESULTS ======\n")
    try:
        dns_results = get_dns_records(domain)
        for record_type, values in dns_results.items():
            print(f"{record_type} Records:")
            for value in values:
                print(f"- {value}")
            print()
    except Exception as e:
        print(f"Error in DNS Enumeration: {e}")

    # BANNER GRABBING
    print("====== BANNER GRABBING RESULTS ======\n")
    try:
        banner_results = grab_banner(domain, ports)
        for port, banner in banner_results.items():
            print(f"[Port {port}] {banner}")
    except Exception as e:
        print(f"Error in Banner Grabbing: {e}")
    print()

    # TECHNOLOGY DETECTION
    print("====== TECHNOLOGY DETECTION (Wappalyzer) ======\n")
    try:
        tech_result = detect_with_wappalyzer(url)
        if isinstance(tech_result, set):
            print("Detected Technologies:")
            for tech in tech_result:
                print(f"- {tech}")
        elif isinstance(tech_result, dict) and "error" in tech_result:
            print(tech_result["error"])
        else:
            print("No technologies detected or unexpected result.")
    except Exception as e:
        print(f"Error in Technology Detection: {e}")

if __name__ == "__main__":
    main()
