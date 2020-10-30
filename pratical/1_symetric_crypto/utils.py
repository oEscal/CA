def save_bytes_file(file_name: str, content: bytes):
   with open(file_name, 'wb') as file:
      file.write(content)


def open_bytes_file(file_name: str) -> bytes:
   with open(file_name, 'rb') as file:
      return file.read()


def read_bytes_file_one_chunk(file_name: str, chunk_size: int):
   with open(file_name, 'rb') as file:
      return file.read(chunk_size)


def read_bytes_file_in_chunks(file_name: str, chunk_size: int, starting_bit: int = 0) -> bytes:
   with open(file_name, 'rb') as file:
      file.seek(starting_bit, 0)
      while True:
         data = file.read(chunk_size)
         if not data:
            break
         yield data
