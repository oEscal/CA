import os
import argparse

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from utils import open_bin_file, save_bin_file, read_bin_file_one_chunk, read_bin_file_in_chunks


PADDING_SIZE = algorithms.AES.block_size//8
CHUNK_SIZE = 2048


def main(key_file: str, input_file: str, output_file: str):
   key = open_bin_file(key_file)

   iv = read_bin_file_one_chunk(input_file, PADDING_SIZE)

   cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
   decriptor = cipher.decryptor()
   unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

   output_content = b''
   for chunk in read_bin_file_in_chunks(input_file, CHUNK_SIZE, starting_bit=PADDING_SIZE):
      output_content += unpadder.update(decriptor.update(chunk))
   output_content += unpadder.finalize()

   save_bin_file(output_file, output_content)


if __name__ == '__main__':
   parser = argparse.ArgumentParser(description="Ciphering a file using the AES.")
   parser.add_argument('--key', '-k', type=str, default="key.bin", help="Symmetric key file name.")
   parser.add_argument('--input', '-i', type=str, required=True, help="File name where the cipher content is stored.")
   parser.add_argument('--output', '-o', type=str, required=True, help="File name where to store the deciphered content.")

   args = parser.parse_args()

   main(args.key, args.input, args.output)
