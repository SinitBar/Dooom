from __future__ import print_function

from vizdoom import *


game = DoomGame()


game.load_config("basic.cfg")

game.init()

actions = [[True, False, False, False], [False, True, False, False], [False, False, True, False], [False, False, False, True]]

episodes = 100

for i in range(episodes):
    print("Episode #" + str(i + 1))
    game.new_episode()
    s = game.get_state()
    for j in range(0, 200):
        game.make_action(actions[3])
    for j in range(0, 40):
        game.make_action(actions[2])
    while not game.is_episode_finished():
        while(not s.game_variables[4]):
            game.make_action(actions[3])
            game.make_action(actions[1])

        for h in range(0, 30):
            game.make_action(actions[0])
            game.make_action(actions[2])
        for h in range(0, 30):
            game.make_action(actions[0])
            game.make_action(actions[1])



