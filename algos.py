class Node:
    def __init__(self, position: str):
        self.edges = []
        self.player = None
        self.position = position

    def remove_player(self):
        self.player = None

    def set_player(self, player: dict):
        self.player = player
    
    def add_edge(self, edge):
        self.edges.append(edge)
        return self


class Edge:
    def __init__(self, first: Node, second: Node):
        self.color = 'R'
        self.first = first
        self.second = second


def init_squad():
    nodes = []
    edges = []

    nodes.append(Node("CM"))
    nodes.append(Node("CM"))
    nodes.append(Node("CB"))
    nodes.append(Node("CB"))
    nodes.append(Node("LM"))
    nodes.append(Node("LW"))
    nodes.append(Node("ST"))
    nodes.append(Node("RW"))
    nodes.append(Node("RM"))
    nodes.append(Node("CB"))
    nodes.append(Node("GK"))

    edge = Edge(nodes[0], nodes[1])
    edges.append(edge)
    nodes[0].add_edge(edge)
    nodes[1].add_edge(edge)

    edge = Edge(nodes[1], nodes[2])
    edges.append(edge)
    nodes[1].add_edge(edge)
    nodes[2].add_edge(edge)

    edge = Edge(nodes[0], nodes[2])
    edges.append(edge)
    nodes[0].add_edge(edge)
    nodes[2].add_edge(edge)

    edge = Edge(nodes[2], nodes[3])
    edges.append(edge)
    nodes[2].add_edge(edge)
    nodes[3].add_edge(edge)

    edge = Edge(nodes[3], nodes[4])
    edges.append(edge)
    nodes[3].add_edge(edge)
    nodes[4].add_edge(edge)

    edge = Edge(nodes[0], nodes[4])
    edges.append(edge)
    nodes[0].add_edge(edge)
    nodes[4].add_edge(edge)

    edge = Edge(nodes[4], nodes[5])
    edges.append(edge)
    nodes[4].add_edge(edge)
    nodes[5].add_edge(edge)

    edge = Edge(nodes[5], nodes[6])
    edges.append(edge)
    nodes[5].add_edge(edge)
    nodes[6].add_edge(edge)

    edge = Edge(nodes[0], nodes[6])
    edges.append(edge)
    nodes[0].add_edge(edge)
    nodes[6].add_edge(edge)

    edge = Edge(nodes[1], nodes[6])
    edges.append(edge)
    nodes[1].add_edge(edge)
    nodes[6].add_edge(edge)

    edge = Edge(nodes[6], nodes[7])
    edges.append(edge)
    nodes[6].add_edge(edge)
    nodes[7].add_edge(edge)

    edge = Edge(nodes[7], nodes[8])
    edges.append(edge)
    nodes[7].add_edge(edge)
    nodes[8].add_edge(edge)

    edge = Edge(nodes[1], nodes[8])
    edges.append(edge)
    nodes[1].add_edge(edge)
    nodes[8].add_edge(edge)

    edge = Edge(nodes[8], nodes[9])
    edges.append(edge)
    nodes[8].add_edge(edge)
    nodes[9].add_edge(edge)

    edge = Edge(nodes[2], nodes[9])
    edges.append(edge)
    nodes[2].add_edge(edge)
    nodes[9].add_edge(edge)

    edge = Edge(nodes[9], nodes[10])
    edges.append(edge)
    nodes[9].add_edge(edge)
    nodes[10].add_edge(edge)

    edge = Edge(nodes[2], nodes[10])
    edges.append(edge)
    nodes[2].add_edge(edge)
    nodes[10].add_edge(edge)

    edge = Edge(nodes[3], nodes[10])
    edges.append(edge)
    nodes[3].add_edge(edge)
    nodes[10].add_edge(edge)

    return nodes, edges


def algo_naive(players, requirements):
    nodes, edges = init_squad()

    categorized_players = {
        "CM": [],
        "CB": [],
        "LM": [],
        "LW": [],
        "ST": [],
        "RW": [],
        "RM": [],
        "GK": []
    }

    for player in players:
        categorized_players[player['pos']].append(player)

    if algo_naive_dc({}, categorized_players, requirements, nodes, edges, 0):
        return nodes
    else:
        return None


def algo_naive_dc(used_players, categorized_players, requirements, nodes, edges, depth):
    if depth == 11:
        return check_requirements(nodes, edges, requirements)

    node = nodes[depth]
    position = node.position
    players = categorized_players[position]

    for player in players:
        used = used_players.get(player['name'], False)
        if used:
            continue

        used_players[player['name']] = True
        node.set_player(player)
        if algo_naive_dc(used_players, categorized_players, requirements, nodes, edges, depth + 1):
            return True
        used_players[player['name']] = False

    return False


def algo_improved(players, requirements):
    leage_nation_mapping = {
        'ANKARA': 'Turkey',
        'Premier League': 'England',
        'La Liga': 'Spain',
        'Serie A': 'Italy',
        'Ligue 1': 'France'
    }
    nodes, edges = init_squad()
    categorized_players = {
        'ANKARA': {
            'Turkey': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'England': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'Spain': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'Italy': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'France': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            }
        },
        'Premier League': {
            'Turkey': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'England': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'Spain': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'Italy': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'France': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            }
        },
        'La Liga': {
            'Turkey': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'England': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'Spain': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'Italy': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'France': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            }
        },
        'Serie A': {
            'Turkey': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'England': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'Spain': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'Italy': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'France': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            }
        },
        'Ligue 1': {
            'Turkey': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'England': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'Spain': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'Italy': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            },
            'France': {
                "CM": [], "CB": [], "LM": [], "LW": [], "ST": [], "RW": [], "RM": [], "GK": []
            }
        }
    }

    player_counts_league = {'ANKARA': 0, 'Premier League': 0, 'La Liga': 0, 'Serie A': 0, 'Ligue 1': 0}
    player_counts_nation = {'Turkey': 0, 'England': 0, 'Spain': 0, 'Italy': 0, 'France': 0}
    sorted_players = sorted(players, key=lambda x: x['rating'], reverse=True)
    
    for player in sorted_players:
        player_counts_league[player['league']] = player_counts_league[player['league']] + 1
        player_counts_nation[player['na']] = player_counts_nation[player['na']] + 1
        categorized_players[player['league']][player['na']][player['pos']].append(player)
    
    player_counts_league = {k: v for k, v in sorted(player_counts_league.items(), key=lambda item: item[1])}
    player_counts_nation = {k: v for k, v in sorted(player_counts_nation.items(), key=lambda item: item[1])}

    if algo_improved_dc(leage_nation_mapping, {}, {}, categorized_players, player_counts_league, player_counts_nation, requirements, nodes, edges, 0):
        return nodes
    else:
        return None


def algo_improved_dc(league_nation_mapping, used_players, used_leagues, players, player_counts_league, player_counts_nation, requirements, nodes, edges, depth):
    if depth == 11:
        return check_requirements(nodes, edges, requirements)

    node = nodes[depth]
    position = node.position
    
    max_league = requirements[2]
    max_league_players = requirements[3]

    leagues_to_check = []

    n_used_leagues = 0

    for league, n_players in used_leagues.items():
        if n_players > 0:
            n_used_leagues += 1

        if n_players < max_league_players:
            leagues_to_check.append(league)
    
    for league in leagues_to_check:
        first_nation = league_nation_mapping[league]
        
        for player in players[league][first_nation][position]:
            used = used_players.get(player['name'], False)
            if used:
                continue
            used_players[player['name']] = True
            used_leagues[league] = used_leagues[league] + 1

            node.set_player(player)
            if algo_improved_dc(league_nation_mapping, used_players, used_leagues, players, player_counts_league, player_counts_nation, requirements, nodes, edges, depth+1):
                return True
            used_players[player['name']] = False
            used_leagues[league] = used_leagues[league] - 1
        
        for nation in player_counts_nation.keys():
            if nation == first_nation:
                continue
            for player in players[league][nation][position]:
                used = used_players.get(player['name'], False)
                if used:
                    continue
                used_players[player['name']] = True
                used_leagues[league] = used_leagues[league] + 1

                node.set_player(player)
                if algo_improved_dc(league_nation_mapping, used_players, used_leagues, players, player_counts_league, player_counts_nation, requirements, nodes, edges, depth+1):
                    return True
                used_players[player['name']] = False
                used_leagues[league] = used_leagues[league] - 1
    
    if n_used_leagues > max_league:
        print("This shouldn't happen, check what's wrong with the algorithm")

    if n_used_leagues == max_league:
        return False

    for league in player_counts_league.keys():
        if used_leagues.get(league, 0) > 0:
            continue
        first_nation = league_nation_mapping[league]
        
        for player in players[league][first_nation][position]:
            used = used_players.get(player['name'], False)
            if used:
                continue
            used_players[player['name']] = True
            used_leagues[league] = used_leagues.get(league, 0) + 1

            node.set_player(player)
            if algo_improved_dc(league_nation_mapping, used_players, used_leagues, players, player_counts_league, player_counts_nation, requirements, nodes, edges, depth+1):
                return True
            used_players[player['name']] = False
            used_leagues[league] = used_leagues[league] - 1
        
        for nation in player_counts_nation.keys():
            if nation == first_nation:
                continue
            for player in players[league][nation][position]:
                used = used_players.get(player['name'], False)
                if used:
                    continue
                used_players[player['name']] = True
                used_leagues[league] = used_leagues.get(league, 0) + 1

                node.set_player(player)
                if algo_improved_dc(league_nation_mapping, used_players, used_leagues, players, player_counts_league, player_counts_nation, requirements, nodes, edges, depth+1):
                    return True
                used_players[player['name']] = False
                used_leagues[league] = used_leagues[league] - 1
        

def check_requirements(nodes, edges, requirements):
    chem_req = requirements[0]
    rating_req = requirements[1]
    n_league_req = requirements[2]
    n_league_player_req = requirements[3]

    rating_sum = 0
    league_counts = {}

    for node in nodes:
        player = node.player
        rating_sum += player['rating']

        league_counts[player['league']] = league_counts.get(player['league'], 0) + 1
    
    if rating_sum / 11 < rating_req:
        return False
    
    count = 0
    for league, p_count in league_counts.items():
        count += 1
        if count > n_league_req or p_count > n_league_player_req:
            return False

    for edge in edges:
        p_first = edge.first.player
        p_second = edge.second.player
        if p_first['team'] == p_second['team']:
            if p_first['na'] == p_second['na']:
                edge.color = 'SG'
            else:
                edge.color = 'G'

        elif p_first['league'] == p_second['league']:
            if p_first['na'] == p_second['na']:
                edge.color = 'G'
            else:
                edge.color = 'Y'

        elif p_first['na'] == p_second['na']:
            edge.color = 'Y'
        else:
            edge.color = 'R'

    chem_sum = 0
    for node in nodes:
        num_red = 0
        for edge in node.edges:
            if edge.color == 'R':
                num_red += 1
            elif edge.color == 'G':
                num_red -= 1
            elif edge.color == 'SG':
                num_red -= 2
            
            if num_red < 0:
                num_red = 0
        chem_sum += (10 - 3 * num_red)

    if chem_sum < chem_req:
        return False
    
    return True
