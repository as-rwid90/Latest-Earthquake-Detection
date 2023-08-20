import requests
from bs4 import BeautifulSoup


def data_extraction():

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitude = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitude = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

    hasil = dict()
    hasil['tanggal'] = tanggal
    hasil['waktu'] = waktu
    hasil['magnitude'] = magnitude
    hasil['kedalaman'] = kedalaman
    hasil['koordinat'] = {'ls': ls, 'bt': bt}
    hasil['lokasi'] = lokasi
    hasil['dirasakan'] = dirasakan

    return hasil


def display_data(result):
    if result is None:
        print("Unable to locate data gempa terkini")
        return

    print('::Gempa Terakhir Berdasarkan BMKG::\n')
    print(f"Tanggal\t\t: {result['tanggal']}")
    print(f"Waktu\t\t: {result['waktu']}")
    print(f"Magnitude\t: {result['magnitude']}")
    print(f"Kedalaman\t: {result['kedalaman']}")
    print(f"Koordinat\t: LS = {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}")
    print(f"Lokasi\t\t: {result['lokasi']}")
    print(f"Dirasakan\t: {result['dirasakan']}")
