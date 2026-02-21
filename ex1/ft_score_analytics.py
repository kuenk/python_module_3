import sys

if __name__ == "__main__":
    """In this program, we get score by input, order it"""
    """and show some basic stadists"""
    print("=== Player Score Analytics ===")
    try:
        first = sys.argv[1]
        total = len(sys.argv) - 1
        scores = [0] * total
        for i in range(total):
            scores[i] = int(sys.argv[i + 1])

        while True:
            flag = 0
            for i in range(total - 1):
                if scores[i] > scores[i + 1]:
                    flag = 1
                    aux = scores[i]
                    scores[i] = scores[i+1]
                    scores[i+1] = aux
            if flag == 0:
                break

        print(f"Scores processed: {scores}")
        print(f"Total players: {total}")
        print(f"Total scores: {sum(scores)}")
        average = sum(scores) / total
        print(f"Average score: {average}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        range = max(scores) - min(scores)
        print(f"Score range: {range}")
    except (ValueError, ZeroDivisionError, IndexError):
        if len(sys.argv) == 1:
            print("No scores provided. Usage python3 ft_score_analytics.py "
                  "<score1> <score2> ...")
        else:
            print("Please, use numbers only.")
