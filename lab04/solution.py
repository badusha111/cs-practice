def winner(names, scores):
    best_index = 0
    for i, score in enumerate(scores):
        if score > scores[best_index]:
            best_index = i
    return names[best_index]


def average(scores):
    return 0.0 if not scores else round(sum(scores) / len(scores), 2)


def ranking(names, scores):
    return [name for _, name in sorted(zip(scores, names), key=lambda x: x[0], reverse=True)]


def above_average(names, scores):
    avg = average(scores)
    return [name for name, score in zip(names, scores) if score > avg]

