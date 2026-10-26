answers = ["b", "a", "d", "c"]
correct = ["b", "c", "d", "c"]

score=0
for ans, cor in zip(answers, correct):
    if ans==cor:
        score+=1
print (f"Score: {score}/4")