#write_file
def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as text_file:
        text_file.write(file_content)

#append file
def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as text_file:
        text_file.write(append_content)

#read file
def read_file(file_name):
    with open(f"{file_name}.txt", encoding='utf-8') as text_file:
        return text_file.read()
