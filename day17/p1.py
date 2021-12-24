INPUT = "input.txt"

def read_input(filename):
    with open(filename) as fp:
        line = next(fp).strip().split(': ')[1]
        x, y = line.split(',')
        x = x.split('=')[1]
        y = y.split('=')[1]
        (xstart, xend) = tuple(map(int, x.split('..')))
        (ystart, yend) = tuple(map(int, y.split('..')))
    return (xstart, xend), (ystart, yend)

def step(pos, vel):
    pos[0] += vel[0]
    pos[1] += vel[1]
    if vel[0] > 0:
        vel[0] -= 1
    elif vel[0] < 0:
        vel[0] += 1
    vel[1] -= 1
    return pos, vel

def pos_in_target(pos, t_x, t_y):
    bounds = []
    if pos[0] < t_x[0]:
        bounds.append('x_min')
    if pos[0] > t_x[1]:
        bounds.append('x_max')
    if pos[1] < t_y[0]:
        bounds.append('y_min')
    if pos[1] > t_y[1]:
        bounds.append('y_max')
    return bounds, False if bounds else True

def check_achieve_target(init_vel, t_x, t_y):
    pos = [0, 0]
    vel = init_vel
    check_traj = True
    while check_traj:
        pos, vel = step(pos, vel)
        bound, target = pos_in_target(pos, t_x, t_y)
        if target:
            return ('', True)
        if 'x_max' in bound:
            return ('x', False)
        if 'y_min' in bound:
            return ('y', False)

def get_max_y(init_vel):
    max_y = 0
    pos = [0, 0]
    vel = init_vel
    inc = True
    while inc:
        pos, vel = step(pos, vel)
        if pos[1] > max_y:
            max_y = pos[1]
        else:
            inc = False
    return max_y

def solve(t_x, t_y):
    max_x = t_x[1]
    max_y = 400
    break_loop = False
    for y in range(max_y, -max_y, -1):
        for x in range(1, max_x+1):
            reason, reached = check_achieve_target([x, y], t_x, t_y)
            if reached:
                break_loop=True
                break
        if break_loop:
            break
    return get_max_y([x, y])

if __name__=='__main__':
    x, y = read_input(INPUT)
    soln = solve(x, y)
    print(soln)
