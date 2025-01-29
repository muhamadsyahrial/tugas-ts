nilai = []
for i in range(10):
    nilai_input = float(input(f"Masukkan nilai ke-{i+1}: "))
    nilai.append(nilai_input)
rata_rata = sum(nilai) / len(nilai)
print(f"Rata-rata dari nilai yang dimasukkan adalah: {rata_rata}")