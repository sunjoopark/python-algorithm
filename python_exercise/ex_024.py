a = [ 75, 25, 6, 73, 43, 46, 31, 13, 60, 90, 5, 43, 35, 65, 100, 28, 83, 95, 35, 45, -1 ]
history = [0] * 11
i = 0
rank = a[i] // 10
if rank >= 0 and rank <= 10:
    history[rank] = history[rank] + 1
i = i + 1
for i in range(len(history)):
    print("{0} 점대 - : {1} 명".format(i*10,history[i]))