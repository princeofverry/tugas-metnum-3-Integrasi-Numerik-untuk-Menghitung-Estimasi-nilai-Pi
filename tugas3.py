import numpy as np
import time


def f(x):
    return 4 / (1 + x**2)


def reimann_integral(a, b, N):
    dx = (b - a) / N
    total = 0.0
    for i in range(N):
        total += f(a + i * dx)
    return total * dx


def trapezoid_integral(a, b, N):
    dx = (b - a) / N
    total = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        total += f(a + i * dx)
    return total * dx


def simpson_integral(a, b, N):
    if N % 2 == 1:
        N += 1  # Simpson's rule requires an even number of intervals
    dx = (b - a) / N
    total = f(a) + f(b)
    for i in range(1, N, 2):
        total += 4 * f(a + i * dx)
    for i in range(2, N-1, 2):
        total += 2 * f(a + i * dx)
    return total * dx / 3


def calculate_error_and_time(method, a, b, N_values, true_value):
    results = {}
    for N in N_values:
        start_time = time.time()
        if method == "reimann":
            integral_value = reimann_integral(a, b, N)
        elif method == "trapezoid":
            integral_value = trapezoid_integral(a, b, N)
        elif method == "simpson":
            integral_value = simpson_integral(a, b, N)
        end_time = time.time()
        error = np.abs(integral_value - true_value)
        results[N] = {
            "integral_value": integral_value,
            "error": error,
            "time": end_time - start_time
        }
    return results


# Nilai referensi pi
true_value = 3.14159265358979323846

# Variasi N
N_values = [10, 100, 1000, 10000]

# Menentukan metode berdasarkan dua digit NIM terakhir
nim_last_two_digits = 62
method_number = nim_last_two_digits % 3

if method_number == 0:
    method_name = "reimann"
elif method_number == 1:
    method_name = "trapezoid"
else:
    method_name = "simpson"

# Hasil pengujian untuk metode yang sesuai
results = calculate_error_and_time(
    method_name, 0, 1, N_values, true_value)

# Fungsi untuk mencetak hasil pengujian


def print_results(method, results):
    print(f"Hasil Pengujian {method}:")
    for N, result in results.items():
        print(f"N = {N}:")
        print(f"  Nilai Integral: {result['integral_value']}")
        print(f"  Galat: {result['error']}")
        print(f"  Waktu Eksekusi: {result['time']} detik")
        print()


# Cetak hasil pengujian
print_results(method_name.capitalize(), results)

# Fungsi untuk menghitung galat RMS


def calculate_rms_error(results):
    errors = [result['error'] for result in results.values()]
    rms_error = np.sqrt(np.mean(np.square(errors)))
    return rms_error


# Hitung galat RMS
rms_error = calculate_rms_error(results)
print(f"Galat RMS: {rms_error}")

# Cetak waktu eksekusi
for N, result in results.items():
    print(f"Waktu Eksekusi untuk N = {N}: {result['time']} detik")
