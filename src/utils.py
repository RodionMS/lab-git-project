import zipfile
# Сжатие и распаковка файлов
def zip_files(file_names, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in file_names:
            zipf.write(file)

def unzip_file(zip_name, extract_to):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)