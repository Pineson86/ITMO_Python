#У меня на компьютере обрабатываются только абсолютные пути файлов
import re

import_file_path = r"C:\Users\User\Documents\Codding\Python\ITMO_Python\home_work#4\phones_emails_for_export.txt"#fthis is a file from which I'll get the contacts

export_file_path = r"C:\Users\User\Documents\Codding\Python\ITMO_Python\home_work#4\imported_phons_emails.txt"#this is a file where I'' write contacts

def get_contacts(import_file_path):
    with open(import_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        phones = re.findall(r'\+?\d{1,4}[-\s]?\(?\d{1,4}\)?[-\s]?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,4}', content)
        emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', content)
    return phones, emails

def write_contacts(export_file_path, get_contacts):
    content = str(get_contacts(import_file_path))
    with open(export_file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return 'Contacts have been successfully saved'

print(write_contacts(export_file_path, get_contacts))