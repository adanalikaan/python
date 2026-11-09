# Senaryo: Bir oyun turnuvasında oyuncuların puanlarını saklayan ve en başarılı oyuncuyu belirleyen sistem geliştirilecektir.

# Öğrenciden Beklenenler
# Oyuncuların isimlerini listeye kaydet.
# Her oyuncunun puanını ayrı listede tut.
# Oyuncuları puanlarıyla birlikte ekrana yazdır.
# En yüksek puanı alan oyuncuyu belirle.
# Listeye yeni bir oyuncu ekle.

oyuncular = ["Ahmet", "Mehmet", "Ali", "Messi"]
puanlar = [87, 92, 77, 95]

for i in range(len(oyuncular)):
    print(oyuncular[i], "-", puanlar[i])

en_yuksek = max(puanlar)

for i in range(len(puanlar)):
    if puanlar[i] == en_yuksek:
        print("En başarılı oyuncu:", oyuncular[i])

oyuncular.append("Kaan")
puanlar.append

print(oyuncular)
print(puanlar)