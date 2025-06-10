import logging
from dns_enum import get_dns_records
from banner_grabber import grab_banner
from tech_detect import detect_with_wappalyzer

def main():
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    # Get user input
    domain = input("Enter domain (e.g., google.com): ").strip()
    url = f"https://{domain}"
    ports = [80, 443, 21, 22, 8080]

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
