import numpy as np

def jacobi_with_steps(A, b, x0, tol=1e-10, max_iter=100):
    n = len(b)
    x = x0.copy()

    print("=== Hasil Iterasi Jacobi ===")
    print("Iterasi |", "  ".join([f"x{i+1:>6}" for i in range(n)]), " |    Norma    |   Perubahan")
    print("-" * (15 + 15 * n))

    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_others = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_others) / A[i, i]

        norm = np.linalg.norm(x_new - x, ord=2)
        diff = np.abs(norm - (np.linalg.norm(x, ord=2) if k > 0 else 0))
        print(f"{k + 1:>7} |", "  ".join([f"{val:>8.6f}" for val in x_new]), f" | {norm:>10.6f} | {diff:>10.6f}")

        if norm < tol:
            break
        x = x_new

    return x

def input_matrix():
    print("Masukkan ukuran matriks (n x n):")
    n = int(input("n = "))
    
    print("Masukkan elemen matriks A (baris per baris):")
    A = []
    for i in range(n):
        row = list(map(float, input(f"Baris {i + 1}: ").split()))
        if len(row) != n:
            raise ValueError("Jumlah elemen dalam baris harus sama dengan n.")
        A.append(row)
    A = np.array(A, dtype=float)
    
    print("Masukkan elemen vektor b:")
    b = list(map(float, input("Vektor b (pisahkan dengan spasi): ").split()))
    if len(b) != n:
        raise ValueError("Vektor b harus memiliki n elemen.")
    b = np.array(b, dtype=float)
    
    print("Masukkan elemen awal x0:")
    x0 = list(map(float, input("Vektor x0 (pisahkan dengan spasi): ").split()))
    if len(x0) != n:
        raise ValueError("Vektor x0 harus memiliki n elemen.")
    x0 = np.array(x0, dtype=float)
    
    return A, b, x0

print("=== Program Iterasi Jacobi ===")
try:
    A, b, x0 = input_matrix()
    tol = float(input("Masukkan toleransi (default 1e-10): ") or 1e-10)
    max_iter = int(input("Masukkan iterasi maksimum (default 100): ") or 100)

    solusi = jacobi_with_steps(A, b, x0, tol=tol, max_iter=max_iter)

    print("Solusi Akhir:")
    print(solusi)
except ValueError as e:
    print("Error: {e}")