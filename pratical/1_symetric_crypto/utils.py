def save_bin_file(file_name: str, content: bin):
   with open(file_name, 'wb') as file:
      file.write(content)
