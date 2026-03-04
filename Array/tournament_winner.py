competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]

def tournament_winner(competitions, results):
    scores = {}
    best_team = ""
    scores[best_team] = 0

    for i, (home_team, away_team) in enumerate(competitions):
        # home_team, away_team = competition
        result = results[i]

        winner = home_team if result == 1 else away_team

        scores[winner] = scores.get(winner, 0) + 3

        if scores[winner] > scores[best_team]:
            best_team = winner
    return best_team

res = tournament_winner(competitions, results)
print(res)
