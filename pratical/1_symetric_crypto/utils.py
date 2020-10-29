def save_bin_file(file_name: str, content: bin):
   with open(file_name, 'wb') as file:
      file.write(content)


def open_bin_file(file_name: str) -> bin:
   with open(file_name, 'rb') as file:
      return file.read()


def read_bin_file_in_chunks(file_name: str, chunk_size: int) -> bin:
   with open(file_name, 'rb') as file:
      while True:
         data = file.read(chunk_size)
         if not data:
            break
         yield data
