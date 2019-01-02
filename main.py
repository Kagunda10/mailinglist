import csv 
from email_validator import validate_email, EmailNotValidError
import argparse
import sys

# filename = "dump.txt"

    def check_email(email):
    try:
        v = validate_email(email) # validate and get info
        email = v["email"] # replace with normalized form
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str, default='',
                        help='What is the File name')
    args = parser.parse_args()
    filename = args.f
    with open (filename, 'r') as f:
        for line in f:
            if ".com" in line:
                email = (line.split('.com')[0]) + '.com'
                if check_email(email) == True:
                    print (email)

main()