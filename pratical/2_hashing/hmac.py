import random
import os

from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.hmac import HMAC


ARRAY_SIZE = 32
NUMBER_TRIALS = 10000


def hmac(key: bytes, string: bytes) -> bytes:
   hmac = HMAC(key, SHA256())
   hmac.update(string)

   return hmac.finalize()


def main():
   # reference: https://cryptography.io/en/latest/hazmat/primitives/mac/hmac.html

   number_of_times_modified = [0]*ARRAY_SIZE
   random_key = os.urandom(ARRAY_SIZE)
   random_byte_array = os.urandom(ARRAY_SIZE)

   original_hmac = hmac(random_key, random_byte_array)

   for n in range(NUMBER_TRIALS):
      modified_key = bytearray()
      index_change = random.randint(0, ARRAY_SIZE - 1)
      for i in range(len(random_key)):
         if i != index_change:
            modified_key.append(random_key[i])
         else:
            modified_key.append(os.urandom(1)[0])
      modified_key = bytes(modified_key)

      new_hmac = hmac(modified_key, random_byte_array)

      for i in range(ARRAY_SIZE):
         if original_hmac[i] != new_hmac[i]:
            number_of_times_modified[i] += 1

   print(number_of_times_modified)


if __name__ == '__main__':
   main()
