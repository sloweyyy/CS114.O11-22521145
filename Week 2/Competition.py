def count_finalists(n, k, scores):
    k_score = scores[k - 1]

    count = 0

    for score in scores:
        if score >= k_score and score > 0:
            count += 1

    return count


n, k = map(int, input().split())
scores = list(map(int, input().split()))

result = count_finalists(n, k, scores)

print(result)
