def winner(names: list[str], scores: list[float]) -> str:
    best_index = 0
    for i in range(0, len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i
    return names[best_index]

def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return round(sum(scores)/len(scores), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    order = sorted(range(len(scores)), key=lambda i: -scores[i])
    return [names[i] for i in order]

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    return [names[i] for i in range(len(scores)) if scores[i] > avg]

def main() -> None:
    names = ["Аня", "Боря", "Вика"]
    scores = [7.0, 9.0, 9.0]

    print("Победитель:      ", winner(names, scores))
    print("Средний результат:", average(scores))
    print("Рейтинг:         ", ranking(names, scores))
    print("Выше среднего:   ", above_average(names, scores))


if __name__ == "__main__":
    main()
