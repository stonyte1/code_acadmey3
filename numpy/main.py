import numpy as np 

# list = np.linspace(0, 9, 9)
# arr = np.array(list)
# print(arr)

# arr_zero = np.zeros(10)
# print(arr_zero)

# arr_oners = np.ones(10)
# print(arr_oners)

# arr_fours = np.ones(10) * 4
# print(arr_fours)

# even = np.arange(0, 100, 2)
# print(even)

# matric = np.linspace(1, 25, 25)
# print(matric[:3, :3])

# print(matric[11])

# sample = np.random.randint(1, 10, 25)
# sample_matrix = sample.reshape(5,5)
# new_matrix = sample_matrix[:3, :3]
# new_matrix1 = new_matrix[:3, :3]
# print(new_matrix1)

# vector = np.random.rand(20)
# print(vector)
# print(np.min(vector))
# print(np.argmin(vector))
# print(vector.dtype)

# numbers = np.random.randint(1, 100, 100)
# print(numbers)
# numbers_90 = numbers > 90
# print(numbers[numbers_90]) 

# print(numbers[numbers % 7 == 0])

# print(np.linspace(0.025, 1, 40).reshape(5, 8))

# matrica = np.arange(2, 1000)
# res = matrica[(matrica ** 0.5) % 1 == 0].reshape(6, 5)
# print(res)


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(np.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

matrix = np.linspace(1, 100, dtype=int)
non_prime_mask = np.array([not is_prime(num) for num in matrix])

filtered_matrix = matrix[non_prime_mask]

print(filtered_matrix)





