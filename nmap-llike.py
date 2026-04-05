#!/usr/bin/env python3

import socket
import subprocess
import threading
from queue import Queue

PORTS = range(1, 1025)
THREADS = 100
TIMEOUT = 1


def resolve(target):
    try:
        return socket.gethostbyname(target)
    except:
        print("[-] Invalid target")
        exit()


def is_up(ip):
    try:
        return subprocess.run(
            ["ping", "-c", "1", ip],
            stdout=subprocess.DEVNULL
        ).returncode == 0
    except:
        return False


def detect_os(ip):
    try:
        out = subprocess.check_output(["ping", "-c", "1", ip]).decode()
        if "ttl=64" in out:
            return "Linux/Unix"
        elif "ttl=128" in out:
            return "Windows"
    except:
        pass
    return "Unknown"


def worker(ip, q, results):
    while not q.empty():
        port = q.get()
        try:
            s = socket.socket()
            s.settimeout(TIMEOUT)

            if s.connect_ex((ip, port)) == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"

                try:
                    s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                    data = s.recv(1024).decode(errors="ignore").strip()
                except:
                    data = ""

                results.append((port, service, data))

            s.close()
        except:
            pass

        q.task_done()


def main():
    target = input("Target: ").strip()
    ip = resolve(target)

    print(f"[+] IP: {ip}")
    print(f"[+] Status: {'UP' if is_up(ip) else 'DOWN'}")
    print(f"[+] OS: {detect_os(ip)}")
    print("[*] Scanning...\n")

    q = Queue()
    results = []

    for p in PORTS:
        q.put(p)

    for _ in range(THREADS):
        threading.Thread(target=worker, args=(ip, q, results), daemon=True).start()

    q.join()

    for port, service, data in sorted(results):
        print(f"{port}/tcp OPEN | {service}")
        if data:
            print(f"  -> {data[:80]}")


if __name__ == "__main__":
    main()
