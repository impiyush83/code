for _ in range(int(input())):
    initial_stack_length, extra_stack_length = list(map(int, input().split()))
    R = list(map(int, input().split()))
    G = list(map(int, input().split()))
    extra = list(map(int, input().split()))
    r_cnt = 0
    g_cnt = 0
    for i in range(0, initial_stack_length + extra_stack_length // 2):
        r = R.pop(0)
        g = G.pop(0)
        if r < g:
            g_cnt += 1
            if extra:
                G.append(extra.pop(0))
                R.append(extra.pop(0))
        else:
            r_cnt += 1
            if extra:
                R.append(extra.pop(0))
                G.append(extra.pop(0))
    if r_cnt == g_cnt:
        print("Tie")
    elif r_cnt > g_cnt:
        print("Radhesh wins")
    else:
        print("Geethakoomaree wins")