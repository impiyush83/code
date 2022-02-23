def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("moving disk", n, "from pole", from_rod, "to pole", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


n1 = 4
TowerOfHanoi(n1, '1', '2', '3')