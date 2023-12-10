def get_connections(x, y, m, n, input_list):
    search_rules = {
        '|': [[0, -1], [0, 1]],
        '-': [[-1, 0], [1, 0]],
        'L': [[0, -1], [1, 0]],
        'J': [[0, -1], [-1, 0]],
        '7': [[0, 1], [-1, 0]],
        'F': [[0, 1], [1, 0]],
        '+': [[1, 0], [0, 1], [-1, 0], [0, -1]]
    }
    connections = []
    if input_list[y][x] in search_rules:
        for x_mod, y_mod in search_rules[input_list[y][x]]:
            x_new = x + x_mod
            y_new = y + y_mod
            if 0 <= x_new < m and 0 <= y_new < n:
                if input_list[y][x] == '+':
                    if input_list[y_new][x_new] == '+':
                        connections.append(f'{x_new}-{y_new}')
                else:
                    connections.append(f'{x_new}-{y_new}')
    return connections


def bfs(graph, start, m, n):
    result = []
    for y in range(n):
        row = []
        for x in range(m):
            row.append(None)
        result.append(row)

    x, y = [int(val) for val in start.split('-')]
    result[y][x] = 0

    q = [start]
    while len(q) > 0:
        v = q.pop(0)
        x_cur, y_cur = [int(val) for val in v.split('-')]
        for e in graph[v]:
            x_edge, y_edge = [int(val) for val in e.split('-')]
            if result[y_edge][x_edge] is None:
                result[y_edge][x_edge] = result[y_cur][x_cur] + 1
                q.append(e)

    return result


def dfs(graph, m, n):
    visited = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(False)
        visited.append(row)

    group = 0
    for y in range(n):
        for x in range(m):
            if visited[y][x] is False:
                v = f"{x}-{y}"
                explore(v, graph, visited, m, n, group)
                group += 1

    return visited


def explore(v, graph, visited, m, n, group):
    x, y = [int(val) for val in v.split('-')]
    visited[y][x] = group

    for e in graph.get(v, []):
        x_e, y_e = [int(val) for val in e.split('-')]
        if visited[y_e][x_e] is False:
            explore(e, graph, visited, m, n, group)


def part1(input_list):
    input_list = input_list.split('\n')
    n = len(input_list)
    m = len(input_list[0])

    S_loc = None
    graph_candidates = {}
    for y in range(n):
        for x in range(m):
            if input_list[y][x] == 'S':
                S_loc = f"{x}-{y}"
            connections = get_connections(x, y, m, n, input_list)

            graph_candidates[f"{x}-{y}"] = []
            for connection in connections:
                graph_candidates[f"{x}-{y}"].append(connection)

    graph = {S_loc: []}
    for source, targets in graph_candidates.items():
        for target in targets:
            if source in graph_candidates[target]:
                val = graph.get(source, [])
                val.append(target)
                graph[source] = val
            if target == S_loc:
                graph[S_loc].append(source)

    result = bfs(graph, S_loc, m, n)

    max_result = 0
    for row in result:
        if max([val if val is not None else 0 for val in row]) > max_result:
            max_result = max([val if val is not None else 0 for val in row])
    return max_result


def part2(input_list):
    input_list = input_list.replace('.', '+')
    input_list = input_list.split('\n')
    n = len(input_list)
    m = len(input_list[0])

    for i, row in enumerate(input_list):
        row = '+' + row + '+'
        input_list[i] = row
    input_list = [''.join(['+' for i in range(m+2)])] + input_list
    input_list.append(''.join(['+' for i in range(m+2)]))

    n = len(input_list)
    m = len(input_list[0])

    for row in input_list:
        print(row)

    S_loc = None
    graph_candidates = {}
    for y in range(n):
        for x in range(m):
            if input_list[y][x] == 'S':
                S_loc = f"{x}-{y}"
            connections = get_connections(x, y, m, n, input_list)

            graph_candidates[f"{x}-{y}"] = []
            for connection in connections:
                graph_candidates[f"{x}-{y}"].append(connection)

    graph = {S_loc: []}
    for source, targets in graph_candidates.items():
        for target in targets:
            if source in graph_candidates[target]:
                val = graph.get(source, [])
                val.append(target)
                graph[source] = val
            if target == S_loc:
                graph[S_loc].append(source)

    result = dfs(graph, m, n)
    edge_group = result[0][0]

    x, y = [int(val) for val in S_loc.split('-')]
    start_group = result[y][x]

    solution = 0
    for y, row in enumerate(result):
        print(''.join([str(val) for val in row]))
        for x, col in enumerate(row):
            # print(col)
            if col not in [edge_group, start_group] and input_list[y][x] == '+':
                # print('Added.')
                solution += 1
    print(solution)
    print()
    return solution
