#!/usr/bin/python3

import socket
import sys
import time
import threading
from queue import Queue

usage = "python3 portxplorer.py TARGET"

print("   ___           _  __  __      _                     ")
print("  / _ \___  _ __| |_\ \/ /_ __ | | ___  _ __ ___ _ __ ")
print(" / /_)/ _ \| '__| __|\  /| '_ \| |/ _ \| '__/ _ \ '__|")
print("/ ___/ (_) | |  | |_ /  \| |_) | | (_) | | |  __/ |   ")
print("\/    \___/|_|   \__/_/\_\ .__/|_|\___/|_|  \___|_|   ")
print("                         |_|                          ")
print("                                                      ")

start_time = time.time()

if len(sys.argv) != 2:
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

print("Scanning target", target)

thread_limit = 100
queue = Queue()

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    conn = s.connect_ex((target, port))
    if not conn:
        if port == 80:
            service = "HTTP"
        elif port == 443:
            service = "HTTPS"
        else:
            service = "Other"
        print(f"Port {port} is OPEN ({service})")
    s.close()

def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()

for port in range(1, 10001):
    queue.put(port)

threads = []
for i in range(thread_limit):
    thread = threading.Thread(target=worker)
    thread.daemon = True
    threads.append(thread)
    thread.start()

queue.join()

end_time = time.time()
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
print(f"Time elapsed: {int(minutes)}m {int(seconds)}s")