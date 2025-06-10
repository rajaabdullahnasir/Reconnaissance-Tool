# DNS Enumeration Module 🔍

This module performs DNS enumeration using Python's `dnspython` library. It's part of a larger Custom Reconnaissance Tool designed for penetration testing and red team exercises.

## 📁 Module Structure

- `dns_enum.py` — Contains the `get_dns_records(domain)` function, which performs DNS record lookups (A, MX, TXT, NS, CNAME, SOA).
- `main.py` — Simple driver script to test the module.

## 🧠 Features

- Retrieves common DNS records:
  - A
  - MX
  - TXT
  - NS
  - CNAME
  - SOA
- Handles and displays errors for each record type.
- Clean, readable output.

## 📌 Requirements

- Python 3.x
- `dnspython` library

### Install `dnspython`

```bash
pip install dnspython
