import math
from heapq import heappop, heappush

def grid_function():
    return [
       [42, 48, 55, 58, 59, 58],
       [44, 50, 56, 'O', 61, 60],
       [45, 49, 57, 'O', 65, 62],
       [39, 45, 55, 60, 'O', 60],
       [38, 40, 50, 55, 59, 58],
       [37, 45, 48, 49, 50, 49],
    ]

max_x = len(grid_function()) - 1  
max_y = len(grid_function()[0]) - 1

def pass_list():
    return [(1, 0), (0, 1), (-1, 0), (0, -1)]

def start_goal_positions():
    return (4, 1), (2, 4)

def heuristic_cost_function(goal):
    intensity = grid_function()[goal[0]][goal[1]]
    return 1 / math.sqrt(intensity)


def A_Star_Search(grid_function, start_goal_positions, heuristic_cost_function, pass_list):
    grid = grid_function()
    start, goal = start_goal_positions()
    priority_queue = [(0, start)]
    came_from = {}
    g_score = {(i, j): float('inf') for i in range(len(grid_function())) for j in range(len(grid_function()[0]))}

    g_score[start] = 0



    while priority_queue:
        current_cost, current_pos = heappop(priority_queue)

        if current_pos == goal:
            path = []
            while current_pos in came_from:
                path.insert(0, current_pos)
                current_pos = came_from[current_pos]
            path.insert(0, start)
            return path

        for move in pass_list():
            x, y = current_pos
            new_pos = (x + move[0], y + move[1])

            if 0 <= new_pos[0] <= max_x and 0 <= new_pos[1] <= max_y:
                if grid[new_pos[0]][new_pos[1]] != 'O':
                    tentative_g_score = g_score[current_pos] + 1

                    if tentative_g_score < g_score[new_pos]:
                        came_from[new_pos] = current_pos
                        g_score[new_pos] = tentative_g_score
                        f_score = tentative_g_score + heuristic_cost_function(new_pos)
                        heappush(priority_queue, (f_score, new_pos))

    return None


path = A_Star_Search(grid_function, start_goal_positions, heuristic_cost_function, pass_list)


if path:
    print("Path:")
    for step in path:
        print(step)
    print("Output: {} is the cell with Carbon Monoxide".format(start_goal_positions()[1]))
else:
    print("No valid path to the goal.")
