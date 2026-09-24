sequences = [
    ("range1", list(range(0, 7))),
    ("range2", list(range(1, 11, 3))),
    ("range3", list(range(5, 0, -1))),
    ("range4", list(range(6, -3, -2)))
]

print(f"{'Name':<8} {'Sequence'}")
print("-" * 30)
for name, seq in sequences:
    print(f"{name:<8} {seq}")