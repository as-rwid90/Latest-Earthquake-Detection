"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 15 Agustus 2023
    Waktu: 10:54:06 WIB
    Magnitudo: 5.8
    Kedalaman: 164 km
    Lokasi: LS = 8.65  BT = 121.51
    Pusat Gempa: 22 km TimurLaut MBAY-NAGEKEO-NTT
    Potensi Tsunami: Tidak berpotensi TSUNAMI
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '15 Agustus 2023'
    hasil['waktu'] = '10:54:06 WIB'
    hasil['magnitudo'] = '5.8'
    hasil['kedalaman'] = '164 km'
    hasil['lokasi'] = {'ls': 8.65, 'bt': 121.51}
    hasil['pusat'] = '22 km TimurLaut MBAY-NAGEKEO-NTT'
    hasil['tsunami'] = 'Tidak berpotensi TSUNAMI'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal\t\t: {result['tanggal']}")
    print(f"Waktu\t\t: {result['waktu']}")
    print(f"Magnitudo\t: {result['magnitudo']}")
    print(f"Kedalaman\t: {result['kedalaman']}")
    print(f"Lokasi\t\t: LS = {result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Pusat Gempa\t: {result['pusat']}")
    print(f"Tsunami\t\t: {result['tsunami']}")


if __name__ == "__main__":
    print("Aplikasi utama")
    result = ekstraksi_data()
    tampilkan_data(result)
