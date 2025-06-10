# 🔍 Reconnaissance-Tool

A modular reconnaissance tool for ethical hacking and penetration testing, developed in Python. This tool helps you gather intelligence about a domain through:

- DNS Enumeration
- Banner Grabbing
- Web Technology Detection (via Wappalyzer)

---

## 📦 Features

- 🔎 **DNS Enumeration**: Retrieves A, MX, TXT, NS, CNAME, and SOA records.
- 🛰️ **Banner Grabbing**: Attempts to connect to common ports and retrieve service banners.
- 🧠 **Technology Detection**: Identifies technologies used by the website using the `Wappalyzer` Python package.

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/rajaabdullahnasir/Reconnaissance-Tool.git
cd Reconnaissance-Tool
```

### 2. Set up a virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python main.py
```

You'll be prompted to enter a domain (e.g., `example.com`). The tool will then display:

- DNS records
- Service banners on common ports (21, 22, 80, 443, 8080)
- Technologies detected on the website

---

## 📂 Modules

- `main.py`: Entry point to the program
- `dns_enum.py`: Handles DNS lookups
- `banner_grabber.py`: Grabs banners from services
- `tech_detect.py`: Uses `Wappalyzer` to identify technologies

---

## 🧱 Requirements

- Python 3.8+
- [Wappalyzer](https://github.com/AliasIO/wappalyzer) (Python port)
- `dnspython`, `requests`, etc.

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📌 Example Output

```
====== DNS ENUMERATION RESULTS ======
A Records:
- 151.101.0.81
...

====== BANNER GRABBING RESULTS ======
[Port 80] No banner (recv timeout)

====== TECHNOLOGY DETECTION (Wappalyzer) ======
- jQuery
- Bootstrap
- Varnish
...
```

---

## 📜 License

This project is licensed under the MIT License. Feel free to modify and use it for educational or ethical penetration testing purposes.

---

## 🙋‍♂️ Author

Developed by:

 **Abdullah Nasir**
- 🔗 [GitHub](https://github.com/rajaabdullahnasir)

 **Syed Ghufran Raza**
- 🔗 [GitHub](https://github.com/SyedGhufranRaza)

 **Bisma Kamran**
- 🔗 [GitHub](https://github.com/Bismakamran)
