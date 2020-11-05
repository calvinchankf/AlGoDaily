def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    reps = []
    l = 3 if len(scores) >= 3 else len(scores)
    for _ in range(l):
        reps.append(
            scores.pop(scores.index(max(scores)))
            )
    return reps



if __name__ == "__main__":
    print(personal_top_three([10, 30]))

