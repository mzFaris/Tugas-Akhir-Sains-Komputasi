import math


def f(x):
    return x + math.exp(x)

def metode_tabel(x_bawah, x_atas, N):
    h = (x_atas - x_bawah) / N
    tabel = []
    
    for i in range(N + 1):
        x = x_bawah + i * h
        y = f(x)
        tabel.append((x, y))
    
    print_tabel(tabel)
    
    for i in range(N):
        x0, fx0 = tabel[i]
        x1, fx1 = tabel[i + 1]
        
        if fx0 == 0:
            return x0
        
        if fx0 * fx1 < 0:
            if abs(fx0) < abs(fx1):
                return x0
            else:
                return x1
    
    return None

def print_tabel(tabel):
    print("Tabel nilai fungsi: ")
    print("x\t\t f(x)")
    print("------------------------")
    for x, fx in tabel:
        print(f"{x:.4f}\t\t {fx:.4f}")

def main():
    x_bawah = float(input("Masukkan nilai batas bawah: "))
    x_atas = float(input("Masukkan nilai batas atas: "))
    N = int(input("Masukkan jumlah pembagian (N): "))
    
    hasil = metode_tabel(x_bawah, x_atas, N)
    if hasil is not None:
        print(f"Akar ditemukan: {hasil}")
    else:
        print("Akar tidak ditemukan dalam interval yang diberikan.")

if __name__ == "__main__":
    main()
