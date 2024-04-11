# Python: Find range overlap and Check if Ranges overlap

def find_range_overlap(a, b):
    return list(range(max(a[0], b[0]), min(a[-1], b[-1]) + 1))


x = range(1, 7)
y = range(5, 10)

overlap = find_range_overlap(x, y)
print(overlap)  # 👉️ [5, 6]

if len(overlap) > 0:
    print('The two ranges overlap')
else:
    print('The two ranges do NOT overlap')