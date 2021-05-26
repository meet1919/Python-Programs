def bat_score(runs, balls, fours, sixes):
    points = runs / 2
    if runs >= 50:
        points = points + 5
    if runs >= 100:
        points = points + 10
    strike_rate = (runs / balls) * 100
    if 80 <= strike_rate <= 100:
        points = points + 2
    if strike_rate > 100:
        points = points + 4
    if fours != 0:
        points = points + int(fours)
    if sixes != 0:
        points = points + (2 * (int(sixes)))


    print('Batscore (This score includes field score if any):', int(points))

def bowl_score(wkts, runs, overs, field):
    points = wkts * 10
    if wkts >= 3:
        points = points + 5
    if wkts >= 5:
        points = points + 10
    economy_rate = runs / overs
    if 3.5 < economy_rate < 4.5:
        points = points + 4
    if 2 < economy_rate < 3.5:
        points = points + 7
    if economy_rate < 2:
        points = points + 10
    if field != 0:
        points = points + 10 * (int(field))
    Score = print('Bowlscore (This score includes field score if any):', points)
