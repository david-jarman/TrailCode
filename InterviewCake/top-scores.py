unsorted_scores = [37,89,41,65,100,91,53]

HIGHEST_POSSIBLE_SCORE = 100

def sort_scores(unsorted_scores, highest_possible_score):
    buckets = [0] * (highest_possible_score + 1)

    for score in unsorted_scores:
        buckets[score] += 1

    sorted_scores = []

    for score, count_of_scores in enumerate(buckets):
        for i in range(count_of_scores):
            sorted_scores.append(score)

    return sorted_scores

print sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
