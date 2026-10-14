def winner(names, scores):
    best_index = 0
    for i in range(0, len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i
    return names[best_index]


def average(scores):
    return 0.0 if not scores else round(sum(scores) / len(scores), 2)


def ranking(names, scores):
    order = sorted(range(len(scores)), key=lambda i: -scores[i])
    return [names[i] for i in order]

def above_average(names, scores):
    avg = average(scores)
    return [names[i] for i in range(len(scores)) if scores[i] > avg]

