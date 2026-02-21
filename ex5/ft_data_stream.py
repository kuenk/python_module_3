def fibonacci_gen():
    """Generate fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_gen():
    """Generate prime numbers"""
    n = 2
    while True:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n

        n += 1


def event_generator(limit):
    """ Create pseudo-random events using fibonacci and prime"""
    """ numbers."""
    players = ['shrek', 'doraemon', 'simba', 'alucard', 'yo']
    actions = ['killed monster', 'found treasure', 'leveled up',
               'wounded', 'fight in the tavern', 'rainy journey']

    fib = fibonacci_gen()
    primes = prime_gen()
    cur_prime = next(primes)
    for i in range(1, limit + 1):
        val = next(fib)

        level = (val % 20) + 1
        player = players[i % len(players)]

        if i == cur_prime:
            action = "found treasure"
            cur_prime = next(primes)
        else:
            action = actions[val % len(actions)]

        yield {"id": i,
               "player": player,
               "level": level,
               "action": action}


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...")

    high_level = 0
    treasure_event = 0
    levelup = 0
    total_processed = 0

    for event in event_generator(100):
        if int(event['id']) <= 10:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        elif event['id'] == 11:
            print("...")

        if event['level'] >= 10:
            high_level += 1
        if event['action'] == 'found treasure':
            treasure_event += 1
        if event['action'] == 'leveled up':
            levelup += 1
        total_processed += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level_up events: {levelup}")

    print("\n=== Generator demostration ===")
    fib_demo = fibonacci_gen()
    print(f"Fibonacci sequence (first 10): "
          f"{[next(fib_demo) for i in range(10)]}")
    prime_demo = prime_gen()
    prime_list = [next(prime_demo) for i in range(5)]
    print(f"Prime numbers (first 5): {prime_list}")
