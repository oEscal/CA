import os
import argparse
import sys

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from utils import open_bin_file, save_bin_file, read_bin_file_in_chunks


PADDING_SIZE = algorithms.AES.block_size//8


def main(key_file: str, input_file: str, output_file: str):
   key = open_bin_file(key_file)

   # setup cipher: AES in CBC mode, w/ a random IV and PKCS #7 padding (similar to PKCS #5)
   iv = os.urandom(PADDING_SIZE)
   cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
   encryptor = cipher.encryptor()
   padder = padding.PKCS7(algorithms.AES.block_size).padder()

   output_content = iv

   # TODO -> analisar como poderá ser melhorada a performance para qualquer tipo de ficheiro de entrada
   for chunk in read_bin_file_in_chunks(input_file, 2048):
      output_content += encryptor.update(padder.update(chunk))
   output_content += encryptor.update(padder.finalize())

   save_bin_file(output_file, output_content)


if __name__ == '__main__':
   parser = argparse.ArgumentParser(description="Ciphering a file using the AES.")
   parser.add_argument('--key', '-k', type=str, default="key.bin", help="Symmetric key file name.")
   parser.add_argument('--input', '-i', type=str, required=True, help="File name to cipher.")
   parser.add_argument('--output', '-o', type=str, required=True, help="File name where to store the ciphered content.")

   args = parser.parse_args()

   main(args.key, args.input, args.output)
