def save_bin_file(file_name: str, content: bin):
   with open(file_name, 'wb') as file:
      file.write(content)


def open_bin_file(file_name: str) -> bin:
   with open(file_name, 'rb') as file:
      return file.read()


def read_bin_file_one_chunk(file_name: str, chunk_size: int):
   with open(file_name, 'rb') as file:
      return file.read(chunk_size)


def read_bin_file_in_chunks(file_name: str, chunk_size: int, starting_bit: int = 0) -> bin:
   with open(file_name, 'rb') as file:
      file.seek(starting_bit, 0)
      while True:
         data = file.read(chunk_size)
         if not data:
            break
         yield data
