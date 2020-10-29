import argparse
import sys

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

from utils import save_bin_file


SALT = b'\x00'
KEY_SIZE = 16


def main(pwd: str, output_file: str):
   kdf = PBKDF2HMAC(hashes.SHA1(), KEY_SIZE, SALT, 1000, default_backend())
   key = kdf.derive(bytes(pwd, 'UTF-8'))

   save_bin_file(output_file, key)


if __name__ == '__main__':
   parser = argparse.ArgumentParser(description="Creation of a symmetric key from a password.")
   parser.add_argument('--password', '-p', type=str, required=True, help="Password to create the symmetric key.")
   parser.add_argument('--output', '-o', type=str, default="key.bin", help="File name where to store the generated key.")

   args = parser.parse_args()

   main(args.password, args.output)
