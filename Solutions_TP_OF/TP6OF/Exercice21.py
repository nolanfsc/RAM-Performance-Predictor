def orientation(A, B, C):
    val = (B[1] - A[1]) * (C[0] - B[0]) - (B[0] - A[0]) * (C[1] - B[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

print(orientation((0, 0), (1, 1), (2, 2)), orientation((0, 0), (1, 0), (1, 1)), orientation((0, 0), (1, 0), (1, -1)))