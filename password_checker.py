import requests
import hashlib

from pip import __main__


def main1():
    password = input("Enter the password you want to check for hacked: ")
    count = hashing_password(password)
    if count:
        print(f"entered password is hacked for {count}  times please change it")
    else:
        print("Carry On, your password is strong enough")

def get_pwned_count(response , hash_to_check):

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h  == hash_to_check:
            return count
    return  0

def get_api_data(half_pass):

    url = "https://api.pwnedpasswords.com/range/"+half_pass
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, please check url")
    return response

def hashing_password(password):

    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_five = sha1password[:5]
    tail = sha1password[5:]
    res= get_api_data(first_five)
    count = get_pwned_count(res, tail)
    return count

main1()




