import numpy as np

def triangularize(A, b):
    n = len(A)
    Aug = np.hstack((A, b.reshape(-1, 1)))
    
    for k in range(n):
        if Aug[k, k] == 0:
            raise ValueError("Pivot utama nol, sistem tidak dapat diselesaikan.")
        
        for i in range(k + 1, n):
            factor = Aug[i, k] / Aug[k, k]
            Aug[i, k:] = Aug[i, k:] - factor * Aug[k, k:]
    
    U = Aug[:, :-1]
    b_new = Aug[:, -1]
    return U, b_new

def back_substitution(U, b):
    n = len(U)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    return x

# Input dari user
def main():
    print("Sistem Persamaan Linear (Ax = b)")
    n = int(input("Masukkan jumlah variabel (n): "))
    
    print("Masukkan elemen matriks A:")
    A = np.array([list(map(float, input(f"Baris {i + 1}: ").split())) for i in range(n)])
    
    print("Masukkan elemen vektor b:")
    b = np.array(list(map(float, input().split())))
    
    print("Proses Triangularisasi...")
    U, b_new = triangularize(A, b)
    print("Matriks Segitiga Atas (U):")
    print(U)
    print("Vektor Baru (b):")
    print(b_new)
    
    print("Proses Substitusi Mundur")
    x = back_substitution(U, b_new)
    print("Jawaban :")
    print(x)

if __name__ == "__main__":
    main()
