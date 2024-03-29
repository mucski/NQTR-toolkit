﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Player")
define a = Character("Alice")
define an = Character("Ann")


# The game starts here.

label start:
    $ block_goout_dialogue = _("To get out you have to take the car keys, (talk to Alice)")

    $ cur_room = rooms[0]
    $ cur_location = locations[cur_room.id_location]
    $ prev_room = rooms[5]
    $ updateBL()
    $ quests["alice"].start()
    $ quests["ann"].start()

    ## call screen room_navigation
    call after_wait

    return
