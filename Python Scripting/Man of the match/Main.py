from Score import *

p1 = {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, 'fours': 10, 'sixes': 0,
      'balls': 119, 'field': 0}
p2 = {'name': 'du Plessis', 'role': 'bat', 'runs': 120, 'fours': 11, 'sixes': 2,
      'balls': 112, 'field': 0}
p3 = {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10,
      'runs': 71, 'field': 1}
p4 = {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10,
      'runs': 45, 'field': 0}
p5 = {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34,
      'field': 0}

players_stats = [p1, p2, p3, p4, p5]

for p in players_stats:
    runs1 = int(p.get('runs', 0))
    balls1 = int(p.get('balls', 0))
    fours1 = int(p.get('fours', 0))
    sixes1 = int(p.get('sixes', 0))
    wkts1 = int(p.get('wkts', 0))
    overs1 = int(p.get('overs', 0))
    field1 = int(p.get('field', 0))

    if p.get('role', 0) == 'bat':
        print('Name :', p.get('name', 0))
        bat_score(runs1, balls1, fours1, sixes1)

    elif p.get('role', 0) == 'bowl':
        print('Name :', p.get('name', 0))
        bowl_score(wkts1, runs1, overs1, field1)

