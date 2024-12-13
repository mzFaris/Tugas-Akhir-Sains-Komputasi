import math


def f(x):
    return x * math.exp(-x) + 1


def main():
    a = float(input("Masukkan nilai a (batas bawah): "))
    b = float(input("Masukkan nilai b (batas atas): "))
    e = float(input("Masukkan toleransi (contoh: 0.0001): "))
    N = int(input("Masukkan iterasi maksimum: "))
    
    akar = bisection(a, b, e, N)
    if akar is not None:
        print(f"Akar ditemukan: {akar}")
    else:
        print("Tidak ditemukan akar dalam interval yang diberikan.")


def bisection(a, b, e, N):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) dan f(b) harus memiliki tanda yang berbeda.")
    
    for i in range(N + 1):
        Fa = f(a)
        Fb = f(b)
        x = (a + b) / 2
        Fx = f(x)
        
        if Fx * Fa < 0:
            b = x
            Fb = Fx
        else:
            a = x
            Fa = Fx
            
        if abs(Fx) < e:
            return x

    return None


if __name__ == "__main__":
    main()
