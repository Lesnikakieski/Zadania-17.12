(lambda n: [print("\n".join(" " * ((n - r) // 2) + "".join("#" if (i - r//2)**2 + (j - r//2)**2 <= (r//2)**2 else " " for j in range(r)) for i in range(r))) for r in (5, 7, 9)])(15)
