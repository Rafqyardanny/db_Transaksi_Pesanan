import pandas as pd
import sqlite3

print("Mulai proses...")

df = pd.read_csv('transaksi_pesanan.csv')

df = df.dropna(subset=['nama_barang', 'jumlah_beli'])

df['nama_barang'] = df['nama_barang'].str.title()
df['status_pengiriman'] = df['status_pengiriman'].str.title()
df['status_pengiriman'] = df['status_pengiriman'].replace('Dikrim', 'Dikirim')

df['total_belanja'] = df['total_belanja'].abs()

df['tanggal_transaksi'] = pd.to_datetime(df['tanggal_transaksi'], dayfirst=True, errors='coerce').dt.strftime('%Y-%m-%d')

conn = sqlite3.connect('db_anterin.db')

df.to_sql('transaksi_bersih', conn, if_exists='replace', index=False)

conn.close()

print("Beres. Cek file db_anterin.db di folder.")