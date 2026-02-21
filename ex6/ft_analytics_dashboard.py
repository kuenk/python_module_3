if __name__ == '__main__':
    print("=== Game Analytics Dashboard ===\n")

    players = [
        {
            "username": "alice",
            "score": 2300,
            "achievements": ["first_kill", "level_10", "boss_slayer",
                             "sharp_shooter", "collector"],
            "active": True,
            "region": "north"
        },
        {
            "username": "bob",
            "score": 1800,
            "achievements": ["first_kill", "level_5", "team_player"],
            "active": True,
            "region": "east"
        },
        {
            "username": "charlie",
            "score": 2150,
            "achievements": ["first_kill", "level_10", "boss_slayer",
                             "explorer", "strategist", "survivor", "veteran"],
            "active": True,
            "region": "central"
        },
        {
            "username": "diana",
            "score": 2050,
            "achievements": ["first_kill", "level_8", "sniper", "collector"],
            "active": False,
            "region": "north"
        }
    ]

    print("=== List Comprehension Examples ===")
    high_scores = [user["username"] for user in players
                   if "score" in user.keys() and user["score"] >= 2000]
    print(f"High scores (>2000): {high_scores}")
    double_scores = [user["score"]*2 for user in players
                     if "score" in user.keys() and user["score"]]
    print(f"Doubled scores: {double_scores}")
    active_players = [user["username"] for user in players
                      if "active" in user.keys() and user["active"]]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {user["username"]: user["score"] for user in players}
    print(f"Player_scores: {player_scores}")
    list_categ = ["high" if user["score"] >= 2200 else "medium"
                  if user["score"] >= 2000 and user["score"] < 2200
                  else "low" for user in players]
    score_cat = {cat: list_categ.count(cat) for cat in set(list_categ)}
    print(f"Score categories: {score_cat}")
    achiv = 0
    achiv = {user["username"]: len(user["achievements"]) for user in players}
    print(f"Achievements counts: {achiv}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {user["username"] for user in players}
    print(f"Unique players: {unique_players}")
    unique_trophies = {achi for user in players for achi in user["achievements"]}
    print(f"all trophies {unique_trophies}")
    common = {achi for achi in[achi for user in players for achi in user["achievements"]]
              if [achi for user in players for achi in user["achievements"]].count(achi) > 1}
    print(f"{common}")
    regions = {user["region"] for user in players}
    print(f"{regions}")


    print ("===\n Combined Analysis ===")
    print(f"Total players: {len(unique_players)}")
    print(f"Total unique achievements: {len(unique_trophies)}")
    avg_score = [user["score"] for user in players]
    print(f"Average score: {sum(avg_score)/len(unique_players)}")
    top = max([(user["username"], user["score"], len(user["achievements"])) for user in players])
    name, score, num_achi = top
    print(f"Top performance: {name}, ({score} points, {num_achi} achievements)")