from sys import exit
from random import randint
from textwrap import dedent

class scene():

    def enter(self):
        print("this scene is not yet configured")
        print("subclass it and implement enter()")
        exit(1)

class engine():

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class death(scene):

    quits = [
        "you died. you kinda suck at this",
        "your mom would be proud... if she were smarter",
        "such a loser",
        "i have a small puppy that's better at this",
        "you're worse than your dad's jokes"
    ]

    def enter(self):
        print(death.quits[randint(0, len(self.quits) - 1)])
        exit(1)

class centralcorridor(scene):

    def enter(self):
        print(dedent("""
            the gothons of planet percal #25 have invaded your ship and
            destroyed your entire crew. you are the last surviving member
            and your last mission is to get the neutron destruct bomb from
            the Weapon Armory, put it in the birdge, and blow the ship up
            after getting into a escape pod

            you're running down the central corridor to the Weapon Armory
            when a gothon jumps out, red scaly skin, dark grimy teeth, and
            evil clown costume flowing around his hate filled body he's
            blocking the door to the Armory and about to pull a weapon to
            blast you
        """))

        action = input('> ')

        if action == "shoot":
            print(dedent("""
                quick on the draw your yank out your blaster and fire it at
                the gothon his clown costume is flowing and moving around
                his body, which throws off your aim your laser hits his
                costume but misses his entirely
                this completely ruins his brand new costume his mother bought
                him, which makes him fly into an insane rage and blast you
                repeatly in the face until you are dead
                then he eat you
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                lucky for you they made you learn gothon insults in the academy
                you tell the one gothon joke you know: the gothon stops, tries
                not to laugh, then brust out laughing and can't move while he's
                laughing you run up and shoot him square in the head putting him
                down then jump through the Weapon Armory door"""))
            return 'laserweaponarmory'

        else:
            print("DOES NOT COMPUTE")
            return 'centralcorridor'

class laserweaponarmory(scene):

    def enter(self):
        print(dedent("""
            you do a dive roll into the Weapon Armory, crouch and scan the
            room for more gothons that might be hiding it's dead quiet, too
            quiet you stand up and run to the far side of the room and find
            the neutron bomb in its container
            there's a keypad lock on the box and you need the code to get the
            bomb out if you get the code wrong 10 times then the lock closees
            forever and you can't get the bomb
            the code is 3 digits
            """))

        code = f"{randint(1,9)}{randint(1,9)randint(1,9)}"
        guess = input('[keypad]> ')
        guesses = 0

        while guess != code and guesses < 10:
            print("bzzzzzddd")
            guesses += 1
            guess = input('[keypad]> ')

        if guess == code:
            print(dedent("""
                    the container clicks open and the seal breaks, letting
                    gas out you grab the neutron bomb and run as fast as you
                    can to the bridge where you must place it in the first spot
                    """))
            return 'thebridge'
        else:
            print(dedent("""
                    the lock buzzes one last time and then you hear a sickening
                    melting sound as the machanism is fused togethr you decide
                    to sit there, and finally the gothons blow up the ship
                    from their ship and you die"""))
            return 'death'

class thebridge(scene):

    def enter(self):
        print(dedent("""
                you brust onto the bridge with the neutron destruct bomb under
                your arm and surprise 5 gothons who are trying to take control
                of the ship each of them has an even uglier clown costume than
                the last thay haven't pulled their weapon out yet as they see
                the active bomb under your arm and don't want to set it off"""))

        action = input('> ')

        if action == "throw the bomb":
            print(dedent("""
                    in a panic you throw the bomb at the group of gothons and
                    make a leap for the door right as you drop it a gothon shoots
                    you in the back killing you as you die you see another gothon
                    frantically try to disarm the bomb you die knowing they will
                    probably blow up when it goes off"""))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                    you point your blaster at the bomb under your arm and the
                    gothons put their hands up and start to sweat your inch
                    backword to the bomb, open it, and then carefully place the
                    bomb on floor, pointing your blaster at it you then jump back
                    through the door, punch the close button and blast the lock
                    so the gothons can't get out now that the bomb is placed
                    you run to the escape pod to get off this can"""))
            return 'escapepod'
        else:
            print("DOES NOT COMPUTE")
            return 'thebridge'

class escapepod(scene):

    def enter(self):
        print(dedent("""
                you rush through the ship desperately trying to make it to
                the escape pod before the whole ship explode it seems like
                hardly any gothons are on the ship, so you run is clear of
                interference you get to the chamber with the escape pod,
                and now need to pick one to take some of them could be damaged
                but you don't have time to look there's 5 pods, which one do
                you take
                """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                    you jump into pod {guess} and hit the eject button the
                    pod escape out into the ovid if space,the implodes as the
                    hull rupyures, crushing your body into jam jelly"""))
            return 'death'

        else:




class map():

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = map('central_corridor')
a_game = engine(a_map)
a_game.play()
