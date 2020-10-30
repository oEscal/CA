import random
import os

from cryptography.hazmat.primitives.hashes import Hash, SHA256


ARRAY_SIZE = 32
NUMBER_TRIALS = 10000


def digest(string: bin) -> bin:
   digest = Hash(SHA256())
   digest.update(string)

   return digest.finalize()


def main():
   # reference: https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes.html

   number_of_times_modified = [0]*ARRAY_SIZE
   random_byte_array = os.urandom(ARRAY_SIZE)

   original_digest = digest(random_byte_array)

   for n in range(NUMBER_TRIALS):
      modified_byte_array = bytearray()
      index_change = random.randint(0, ARRAY_SIZE - 1)
      for i in range(len(random_byte_array)):
         if i != index_change:
            modified_byte_array.append(random_byte_array[i])
         else:
            modified_byte_array.append(os.urandom(1)[0])
      modified_byte_array = bytes(modified_byte_array)

      new_digest = digest(modified_byte_array)

      for i in range(ARRAY_SIZE):
         if original_digest[i] != new_digest[i]:
            number_of_times_modified[i] += 1

   print(number_of_times_modified)


if __name__ == '__main__':
   main()
