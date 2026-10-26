scores = [12, 17, 9, 15, 14]
index_best = 0
score_best = -1

for ind, scr in enumerate (scores, start=1):
    if score_best<scr:
        score_best = scr
        index_best = ind
print(f"Best: {score_best}, (student# {index_best})")