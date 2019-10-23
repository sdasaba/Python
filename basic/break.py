total = 0
scores = [80,60,70,90]

for s in scores:
    total += s
    if total >= 200:
        break
    else:
        continue

print(total)