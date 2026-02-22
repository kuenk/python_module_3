def achi_analytics(players):
    """Search and show unique and common achivements"""

    repeat_trophies = set()
    total_trophies = set()
    all_trophies = players.values()

    for trophies in players.values():
        current = total_trophies.intersection(trophies)
        print(f"current {current}")
        repeat_trophies = repeat_trophies.union(current)
        total_trophies = total_trophies.union(trophies)

    unique_trophies = total_trophies.difference(repeat_trophies)
    common_trophies = set.intersection(*all_trophies)

    print("\n=== Achievement Analytics ===")
    total = len(total_trophies)
    print(f"All unique achievements: {total_trophies}")
    print(f"Total unique achievements: {total}")

    print(f"Common to all players: {common_trophies}")
    print(f"Rare achievements (1 player): {unique_trophies}")


if __name__ == "__main__":
    print("=== Achievements tracker system ===\n")
    players = {
        "alice": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "bob": {"first_kill", "level_10", "boss_slayer", "collector"},
        "charlie": {"level_10", "treasure_hunter", "boss_slayer",
                    "speed_demon", "perfectionist"}
    }

    for player, trophies in players.items():
        print(f"Player: {player} {trophies}")
    achi_analytics(players)

    print(f"\nAlice vs Bob common: "
          f"{players['alice'].intersection(players['bob'])}")
    print(f"Alice unique: {players['alice'].difference(players['bob'])}")
    print(f"Bob unique: {players['bob'].difference(players['alice'])}")
