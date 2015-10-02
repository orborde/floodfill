WIDTH = 10
HEIGHT = 10

START = (0,0)

def inbounds(r, c):
    return (r >= 0 and r < HEIGHT and
            c >= 0 and c < WIDTH)

def neighbors(r, c):
    ret = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
    return filter(lambda t: inbounds(*t), ret)

def floodfill_dfs(sr, sc):
    visited = set()
    frontier = [(sr,sc)]
    max_frontier_size = -1

    while len(frontier) > 0:
        max_frontier_size = max(max_frontier_size, len(frontier))
        r, c = frontier.pop()
        visited.add((r,c))

        for nr,nc in neighbors(r,c):
            if (nr,nc) in visited:
                continue

            visited.add((nr,nc))
            frontier.append((nr,nc))

    print "Depth:", max_frontier_size
    return visited

def floodfill_bfs(sr, sc):
    visited = set()
    frontier = [(sr,sc)]
    max_frontier_size = -1

    while len(frontier) > 0:
        max_frontier_size = max(max_frontier_size, len(frontier))
        new_frontier = []

        for r,c in frontier:
            visited.add((r,c))

            for nr,nc in neighbors(r,c):
                if (nr,nc) in visited:
                    continue

                visited.add((nr,nc))
                new_frontier.append((nr,nc))

        frontier = new_frontier

    print "Breadth:", max_frontier_size
    return visited

import itertools

def test_floodfill(func):
    visited = func(*START)
    allnodes = set(itertools.product(range(WIDTH), range(HEIGHT)))
    assert visited == allnodes

test_floodfill(floodfill_dfs)
test_floodfill(floodfill_bfs)
