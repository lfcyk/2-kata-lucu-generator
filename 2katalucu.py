import sys, random

kata = ['lagu', 'ini', 'sakral', 'ga', 'bisa', 'seenak', 'jidat', 'di', 'persembahkan', 'buat', 'pacar', 'jauh', 'daripada', 'itu', 'tentang', 'cinta', 'yang', 'tulus', 'hingga', 'berbeda', 'alam', 'nanti', 'lagu', 'universal', 'dan', 'saya', 'untuk', 'mamah', 'karena', 'setiap', 'pagi', 'menjelang', 'beliau', 'selalu', 'ada', 'samping', 'aman', 'dekatnya', 'sampai', 'jadi', 'debu', 'setan', 'biadab', 'kau', 'brenton!', '', 'nangiss', 'nonton', 'videonya', 'turut', 'berduka', 'cita', '49', 'orng', 'dibunuh', 'saat', 'solat', 'jumat', 'menembak', 'aturan', 'tata', 'caranya', 'semoga', 'korban2', 'hari', 'jumat', 'dalam', 'masjid', 'syahid', 'pray', 'for', 'new', 'zeland', 'god', 'bless', 'indonesia', 'cara', 'melihat', 'jin', 'yang', 'menempel', 'di', 'tubuh', 'kita', 'jika', 'kamu', 'berada', 'rumah', 'berdirilah', 'menghadap', 'ke', 'arah', 'kiblat', 'tengok', 'atas', 'beberapa', 'pejam', 'mata', 'rapat', 'baca', 'doa', 'sebisa', 'niat', 'hati', 'mengetahui', 'jin', 'apa', 'yg', 'badan', 'tarik', 'nafas', 'perlahan-lahan', 'lalu', 'lepaskan', 'sambil', 'terus', 'mengucapkan', 'tundukkan', 'kepala', 'dengan', 'perlahan', 'buka', 'kedua', 'bahu', 'jalan']
print("2 Kata Lucu!")

print("digenerate secara random dari", len(kata) ,"kata")

while True:
    kata1 = random.choice(kata)
    kata.remove(kata1)
    kata2 = random.choice(kata)

    print("\n{} {}\n".format(kata1.upper(),kata2.upper()), file=sys.stderr)
    kata.append(kata1)

    lagi = input("mau lagi gak? y? n?")
    if lagi.lower() == "n":
        break