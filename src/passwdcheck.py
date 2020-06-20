import requests
import hashlib
import argparse
import getpass


def request_api_data(chars: str):
    url = 'https://api.pwnedpasswords.com/range/' + chars
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, c in hashes:
        if h.strip() == hash_to_check:
            return int(c)
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main():
    while True:
        try:
            pwd = getpass.getpass(prompt="Enter your password (Use Ctrl-C to leave): ")
        except KeyboardInterrupt:
            print("\nBye")
            break

        count = pwned_api_check(pwd)
        if count > 0:
            print(f"[{pwd}] was FOUND {count} times")
        else:
            print(f"[Your Password] was not found")
