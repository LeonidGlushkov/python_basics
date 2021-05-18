src = [12, 15, 345, 654, 232, 1, 32, 555, 4, 545, 768, 78, 23]
result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(result)
