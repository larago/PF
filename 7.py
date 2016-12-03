# from random import random

# time = 5
# car_positions = [1, 1, 1]

# while time:
#     time -= 1

#     print ''
#     for i in range(len(car_positions)):
#         if random() > 0.3:
#             car_positions[i] += 1

#         print '-' * car_positions[i]

###

# from random import random

# def move_cars():
#     for i, _ in enumerate(car_positions):
#         if random() > 0.3:
#             car_positions[i] += 1

# def draw_car(car_positions):
#     print '_' * car_positions

# def run_step_of_race():
#     global time
#     time -= 1
#     move_cars()

# def draw():
#     print
#     for car_position in car_positions:
#         draw_car(car_position)

# time = 5
# car_positions = [1, 1, 1]

# while time:
#     run_step_of_race()
#     draw()

###

from random import random

def move_cars(car_positions):
    return map(lambda x: x + 1 if random() > 0.3 else x,
                car_positions)

def output_car(car_position):
    return '_' * car_position

def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}

def draw(state):
    print ''
    print 'n'.join(map(output_car, state['car_positions']))

def race(state):
    draw(state)
    if state['time']: race(run_step_of_race(state))

race({'time': 5,
      'car_positions': [1, 1, 1]})