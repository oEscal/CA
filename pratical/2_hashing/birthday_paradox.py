import random
import os

from cryptography.hazmat.primitives.hashes import Hash, SHA256, MD5


ARRAY_SIZE = 32
NUMBER_BYTES_COMPARE = 2         # for SHA256 THERE ARE 32 BYTES FOR EXAMPLE, UNFEASIBLE
NUMBER_TRIALS = 1000


def digest(string: bytes) -> bytes:
   digest = Hash(SHA256())
   digest.update(string)

   return digest.finalize()


def main():
   # reference: https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes.html

   total_number_iterations = 0

   for i in range(NUMBER_TRIALS):
      random_bytes = os.urandom(ARRAY_SIZE)
      original_digest = digest(random_bytes)

      number_trials = 0
      while True:
         number_trials += 1

         new_random_bytes = os.urandom(ARRAY_SIZE)
         new_digest = digest(new_random_bytes)

         if original_digest[:NUMBER_BYTES_COMPARE] == new_digest[:NUMBER_BYTES_COMPARE]:
            print(f"COLISION AT ITERATION {number_trials} FOR {NUMBER_BYTES_COMPARE*8} BITS OF DIGEST")
            total_number_iterations += number_trials
            break

   print("\n\n\n\n\n")
   print(f"Average number of iterations necessary for collision for {NUMBER_BYTES_COMPARE*8} bits of digest: {total_number_iterations/NUMBER_TRIALS}")


if __name__ == '__main__':
   main()
