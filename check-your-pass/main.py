import requests
import hashlib
import sys

def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    return next((int(count) for h, count in hashes if h == hash_to_check), 0)

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def check_password_strength(password):
    if len(password) < 8 or password.isdigit():
        return 'Weak'
    if any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        return 'Strong'
    return 'Moderate'

def main(args):
    for password in args:
        count = pwned_api_check(password)
        strength = check_password_strength(password)
        if count:
            print(f'{password}: Found {count} times, consider changing it.\nStrength: {strength}\n')
        else:
            print(f'{password}: Not found.\nStrength: {strength}')
    return 'Done!'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python script.py <password>...')
        sys.exit(1)
    sys.exit(main(sys.argv[1:]))