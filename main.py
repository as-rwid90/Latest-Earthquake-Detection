"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
import gempa_terkini

if __name__ == "__main__":
    print('Main App')
    result = gempa_terkini.data_extraction()
    gempa_terkini.display_data(result)
