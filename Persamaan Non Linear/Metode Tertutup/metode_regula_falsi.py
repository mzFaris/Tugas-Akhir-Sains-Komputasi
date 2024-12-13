import math


def f(x):
    return x * math.exp(-x) + 1


def main():
    a = float(input("Masukkan nilai a (batas bawah): "))
    b = float(input("Masukkan nilai b (batas atas): "))
    e = float(input("Masukkan toleransi (contoh: 0.0001): "))
    n = int(input("Masukkan iterasi maksimum: "))
    
    hasil = regula_falsi(a, b, e, n)
    if hasil is not None:
        print(f"Akar ditemukan: {hasil}")
    else:
        print("Tidak ditemukan akar dalam interval yang diberikan.")


def regula_falsi(a, b, e, n):
    for i in range(1, n + 1):
        Fa = f(a)
        Fb = f(b)
        
        x = (Fb * a - Fa * b) / (Fb - Fa)
        Fx = f(x)
        error = abs(Fx)
        
        if Fx * Fa < 0:
            b = x
            Fb = Fx
        else:
            a = x
            Fa = Fx
            
        if error < e:
            return x

    return None


if __name__ == "__main__":
    main()
