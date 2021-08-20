def tally(rows):
    
    match_table = {} # Team_Name: Played_Maches, wins, draws, losses, scores
    def update_win(team_name):
        if team_name in match_table:
            match_table[team_name][0] +=1
            match_table[team_name][1] +=1
            match_table[team_name][4] +=3
        else:
            match_table[team_name] = [1, 1, 0, 0, 3]

    def update_draw(team_name):
        if team_name in match_table:
            match_table[team_name][0] +=1
            match_table[team_name][2] +=1
            match_table[team_name][4] +=1
        else:
            match_table[team_name] = [1, 0, 1, 0, 1]
    
    def update_loss(team_name):
        if team_name in match_table:
            match_table[team_name][0] +=1
            match_table[team_name][3] +=1
        else:
            match_table[team_name] = [1, 0, 0, 1, 0]
        
    
    for i in range(len(rows)):
        team_a, team_b, result = (rows[i].split(';'))
        
        if result == 'win':
            update_win(team_a)
            update_loss(team_b)
        elif result =='draw':
            update_draw(team_a)
            update_draw(team_b)
        elif result == 'loss':
            update_win(team_b)
            update_loss(team_a)

    match_table  = dict(sorted(match_table.items(), key = lambda x: x[0]))# sorting by the name in alphabetical order
    header = ["Team                           | MP |  W |  D |  L |  P"]
    table = [team.ljust(30, ' ') + ''.join([' | ' + str(v).rjust(2, ' ') for v in score])
        for team, score in sorted(match_table.items(), key = lambda x: str(x[1][4]), reverse = True)]# sorting by the total scores
    
    return header+table

    # table_format='{:<30} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3}'
    # return '\n'.join( [ table_format.format('Team', 'MP', 'W', 'D', 'L', 'P') ]
    #         + [ table_format.format(t['Team'],t['MP'],t['W'],t['D'],t['L'], t['P'])
    #             for t in sorted(sorted(match_table.values(), key=lambda s:s['Team']), key=lambda r:r['P'], reverse=True) 
    #     ])
    
# rows = [
#     "Allegoric Alaskans;Blithering Badgers;win",
#             "Blithering Badgers;Courageous Californians;win",
#             "Courageous Californians;Allegoric Alaskans;loss",
# ]

# print(tally(rows))

# rows = [
#             "Allegoric Alaskans;Blithering Badgers;win",
#             "Devastating Donkeys;Courageous Californians;draw",
#             "Devastating Donkeys;Allegoric Alaskans;win",
#             "Courageous Californians;Blithering Badgers;loss",
#             "Blithering Badgers;Devastating Donkeys;loss",
#             "Allegoric Alaskans;Courageous Californians;win",
#         ]
# print(tally(rows))
