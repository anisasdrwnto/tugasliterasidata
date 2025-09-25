import json
import pandas as pd

# 1. Baca file JSON
with open("Anisa Sudarwanto_V3925019.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 2. Buat ExcelWriter
with pd.ExcelWriter("Data_JSON.xlsx", engine="openpyxl") as writer:
    # Loop setiap key (data_lokasi, data_visual, dst.)
    for key, value in data.items():
        # Pastikan value berupa list of dict
        if isinstance(value, list):
            df = pd.DataFrame(value)
            # Tulis ke sheet dengan nama sesuai key
            df.to_excel(writer, sheet_name=key, index=False)

print("✅ File Excel berhasil dibuat: Data_JSON.xlsx")
