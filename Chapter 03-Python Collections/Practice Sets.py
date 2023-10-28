L1 = [1, 5, 5]
L2 = [3, 4, 5, 5, 10]
L3 = [5, 5, 10, 20]

# Typecasting into sets

s1 = set(L1)
s2 = set(L2)
s3 = set(L3)

# Join using intersection_update function

s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)

final_list = list(final_set)
print(final_list)

