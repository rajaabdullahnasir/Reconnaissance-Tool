from dns_enum import get_dns_records

domain = "google.com"
results = get_dns_records(domain)

print ("====== DNS ENUMERATION RESULTS ======\n")

for record_type, values in results.items():
    print(f"record_type Records:")
    for value in values:
        print (f"-{value}")