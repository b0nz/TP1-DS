data = {
  "jenis_kelamin": ["Laki-Laki", "Laki-Laki", "Perempuan", "Perempuan", "Laki-Laki", "Laki-Laki", "Perempuan", "Perempuan", "Laki-Laki", "Perempuan"],
  "umur": [20, 35, 26, 27, 21, 22, 32, 26, 25, 20],
  "gaji": [8000000, 14000000, 10000000, 12000000, 9000000, 11000000, 15000000, 8000000, 9000000, 10000000],
  "transportasi": ["Kendaraan Pribadi", "Kendaraan Umum", "Kendaraan Umum", "Kendaraan Pribadi", "Kendaraan Pribadi", "Kendaraan Pribadi", "Kendaraan Umum", "Kendaraan Umum", "Kendaraan Umum", "Kendaraan Pribadi" ],
}

def jabatan(gaji):
  if gaji >= 8000000 and gaji < 10000000:
    return "Officer"
  elif gaji >= 10000000 and gaji < 12000000:
    return "Supervisor"
  elif gaji >= 12000000 and gaji < 15000000:
    return "Assisten Manager"
  elif gaji >= 15000000:
    return "Manager"
  else:
    return "Jabatan Tidak Ditemukan"

def cari_jabatan():
  gaji = int(input("Masukkan gaji: "))
  print("Jabatan: ", jabatan(gaji))
  print("==============================================\n")

def tampilkan_gaji():
  gaji_terbesar = max(data["gaji"])
  gaji_terkecil = min(data["gaji"])
  print("Gaji terbesar: ", format(gaji_terbesar, ",.2f"))
  print("Gaji terkecil: ", format(gaji_terkecil, ",.2f"))
  print("==============================================\n")

def tampilkan_data():
  for i in range(len(data["jenis_kelamin"])):
    print("Jenis kelamin: ", data["jenis_kelamin"][i])
    print("Umur: ", data["umur"][i])
    print("Gaji: ", format(data["gaji"][i], ",.2f"))
    print("Transportasi: ", data["transportasi"][i])
    print("Jabatan: ", jabatan(data["gaji"][i]))
    print("----------------------------------------------")
  tampilkan_gaji()

def get_choice():
  try:
    choice = int(input("Masukkan pilihan: "))
  except ValueError:
    print("Invalid choice.\n")
    return None

  if choice < 1 or choice > 4:
    print("Invalid choice.\n")
    return None
  return choice

def menu():
  while True:
    print("MENU")
    print("==============================================")
    print("1. Cari jabatan berdasarkan gaji")
    print("2. Tampilkan gaji terbesar dan terkecil")
    print("3. Tampilkan data")
    print("4. Keluar")
    print("==============================================")

    pilihan = get_choice()
    if pilihan is not None:
      if pilihan == 1:
        cari_jabatan()
      elif pilihan == 2:
        tampilkan_gaji()
      elif pilihan == 3:
        tampilkan_data()
      elif pilihan == 4:
        break
      else: 
        print("Pilihan tidak tersedia\n")
      
if __name__ == "__main__":
  menu()