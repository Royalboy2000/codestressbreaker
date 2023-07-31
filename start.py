import os
import requests
import threading
import time
import pyfiglet
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def make_requests(url):
    while True:
        response = requests.get(url)
        time.sleep(1)

def get_input_with_color(prompt):
    return input(Fore.YELLOW + prompt + Style.RESET_ALL)

def get_available_memory():
    mem_info = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    return mem_info / (1024.0 ** 3)

def main():
    # Print credits
    credits = pyfiglet.figlet_format("stress Test Script")
    print(Fore.CYAN + credits + Style.RESET_ALL)
    print(Fore.MAGENTA + "Instagram: https://www.instagram.com/s.a.m.i.r_012/")
    print(Fore.MAGENTA + "GitHub: https://github.com/Royalboy2000" + Style.RESET_ALL)

    ascii_art = pyfiglet.figlet_format("Codebreakers")
    print(Fore.GREEN + ascii_art + Style.RESET_ALL)

    url = get_input_with_color("Enter the URL to test: ")
    time_duration = int(get_input_with_color("Enter the test duration in seconds: "))
    req_per_sec = int(get_input_with_color("Enter the requests per second: "))
    ram_gb = int(get_input_with_color("Enter the amount of RAM you have in GB: "))

    threads = max(1, ram_gb // 2)
    delay = 1 / req_per_sec
    divided_ram_mb = ram_gb * 1024

    print(Fore.BLUE + f"Available memory: {ram_gb:.2f} GB" + Style.RESET_ALL)

    for _ in range(threads):
        t = threading.Thread(target=make_requests, args=(url,))
        t.daemon = True
        t.start()

    print(Fore.YELLOW + f"Load testing {url} for {time_duration} seconds with {req_per_sec} requests per second and {threads} threads.")
    print(Fore.RED + "Press Ctrl+C to stop the load test." + Style.RESET_ALL)

    try:
        subprocess.run(["node", f"--max-old-space-size={divided_ram_mb}", "codebreaker.js", url, str(time_duration), str(req_per_sec), str(threads)], check=True)
    except subprocess.CalledProcessError:
        print(Fore.RED + "An error occurred while running 'codebreaker.js'" + Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "Load test stopped by user." + Style.RESET_ALL)

if __name__ == "__main__":
    main()

