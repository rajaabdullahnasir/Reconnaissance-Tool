import socket

def grab_banner(host, ports):
    banners = {}
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)
                s.connect((host, port))
                try:
                    banner = s.recv(1024).decode(errors="ignore").strip()
                    if banner:
                        banners[port] = banner
                    else:
                        banners[port] = "No banner received"
                except socket.timeout:
                    banners[port] = "No banner (recv timeout)"
        except Exception as e:
            banners[port] = f"Error: {e}"
    return banners
