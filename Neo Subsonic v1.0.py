# Kirklen Allen
# Neo Subsonic v1.0
#Text Based Sci Fi Runner

#Play Menu
print('Neo Subsonic a Text Sci Fi Runner')
print('<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>')
print('Collect the Instruments your friends need before the Big Show Tonight')
print('<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>')
print('Move around by typing Go North, Go South, Go East, or Go West')

#Dictionary Function to store Valu eof Rooms
Rooms = {
        'Main Entrance': {'South': 'School Eco Center', 'East': 'Percussion Hall'},
        'Percussion Hall': {'West': 'Main Entrance'},
        'School Eco Center': {'North': 'Main Entrance',
                        'West': 'String Hall', 'South': 'Solar Court Yard'},
        'String Hall': {'East': 'School Eco Center'},
        'Solar Court Yard': {'West': 'Practice Simulator 1', 'East': 'Woodwind Hall',
                        'South': 'UV Tech Room'},
        'UV Tech Room': {},
        'Woodwind Hall': {'West': 'Solar Court Yard', 'South': 'Practice Simulator 2',
                        'North': 'Brass Hall'},
        'Practice Simulator 2': {'North': 'Woodwind Hall'},
        'Brass Hall': {'South': 'Woodwind Hall'}}

#Player Begins At Main Entrance
startRoom = 'Main Entrance'
currentRoom = startRoom
NewRoom = Rooms

#Player Location Shown

#Player Moving Input
while True:
    print("I'm in the " + currentRoom + ", Where should I go?")
    move = input("Go East to move:")
    break
# Percussion Hall
if move == 'Go East':
    currentRoom = 'Percussion Hall'
    print("\nI'm in the {} look what I found!".format('Percussion Hall'))
    print('Found the Celeste')
    print('Inventory:', 'Celeste')
    print('Let me go Back to the Main Entrance')

currentRoom = 'Main Entrance'

print("We are back at the {} maybe we should Go South.".format('Main Entrance'))
print('Inventory:')
move = input("Enter a move:")


# School Eco Center
if move == 'Go South':
    currentRoom = 'School Eco Center'
    print('Inventory:', 'Celeste')
    print("Im in the {} there is nothing better than fresh plants!"
          "We should head West.".format('School Eco Center'))
move = input("Enter a move:")


# String Hall
if move == 'Go West':
    currentRoom = 'String Hall'
    print("\nWe are in {} I love to hear the strings play hear! Haha get it? Hear.".format('String Hall'))
    print('Found a Violin')
    print('Inventory:', 'Celeste', 'Violin')
    print("Tip: Maybe we should go back to School Eco Center move the adjacent direction.")
move = input("Enter a move:")

if move == 'Go East':
    print("\nBack in the {} I could sit here all the time but now is not the time! "
          "\nWe should go down there.".format('School Eco Center'))
    print('Inventory:', 'Celeste', 'Violin')
move = input("Enter a move:")

# Solar Court Yard
if move == 'Go South':
    currentRoom = 'Solar Court Yard'
    print("\nI remember the first time I ever saw the {} this is breathtaking. "
          "\nOur school is self sustained.".format('Solar Court Yard'))
    print("Tip: Theres a sound over West. What is that?")
    print('Inventory:', 'Celeste', 'Violin')
move = input("Enter a move:")

#Practice Simulator
if move == 'Go West':
    print("I love the {} someone left the Unreal Engine Environment running but "
          "\nI'm glad I came here.".format('Practice Simulator'))
    print('Found the 3d Printed Cello')
    print('Inventory:', 'Celeste', 'Violin', 'Cello')
    print("Tip:If you hear Bass of the West go East!")
move = input("Enter a move:")


# Solar Court Yard
if move == 'Go East':
    currentRoom = 'Solar Court Yard'
    print("\nWe are back in the {} dont go in "
          "\nthe room down there its self cleaning.".format('Solar Court Yard'))
    print('Inventory:', 'Celeste', 'Violin', 'Cello')
    print('Tip: I have a feeling we should not go North, or West')
move = input("Enter a move:")


# Game Over
if move == 'Go South':
    print('You tripped a senor and sounded the alarm from the UV Light. Sorry! Try Again.')
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>')
    print('<<<<<<<<<<<<<<<<<<<<<<<Game Over>>>>>>>>>>>>>>>>>>>')
    print('<<<<<<<<<<<<<<<Thank You For Playing!>>>>>>>>>>>>>>')
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>')

# Woodwind Hall
if move == 'Go East':
    currentRoom = 'Woodwind Hall'
    print("We made it to {} there is a shimmer coming from the glow of the moon over there.".format('Woodwind Hall'))
    print("Found the Crystal Clarinet")
    print('Inventory:', 'Celeste', 'Violin', 'Cello', 'Clarinet')
    print('Tip: Someone left another Simulator on we cant waste Solar energy. Just go South and cut it off.')
    move = input("Enter a move:")

# Practice Simulator 2
if move == 'Go South':
    currentRoom = 'Practice Simulator 2'
    print("As I turn off the {} I see a flute that camouflages to the room that is amazing.".format('Practice Simulator 2'))
    print("Found the Flute")
    print('Inventory:', 'Celeste', 'Violin', 'Cello', 'Clarinet', 'Flute')
    print("Tip:Lets Go Back to the Hall ")
move = input("Enter a move:")

if move == 'Go North':
    currentRoom = 'Woodwind Hall'
    print("We are back in {}. The Only place we can go from here is up".format('Woodwind Hall'))
    print('Inventory:', 'Celeste', 'Violin', 'Cello', 'Clarinet', 'Flute')
    print("Tip: The statement might be literal.")
move = input("Enter a move:")

# Brass Hall
if move == 'Go North':
    currentRoom = 'Brass Hall'
    print("The one and only {} some call this instrument the roar of the Orchestra or maybe that is just me. :P"
          "\n Whats that?!".format('Brass Hall'))
    print("Found the Proto Tuba this is version 2 be Careful!")
    print('Inventory:', 'Celeste', 'Violin', 'Cello', 'Clarinet', 'Flute', 'Tuba')

    #Completion Message
    print("Congratulations You Gathered every Instrument before the show.")
    print('Y*********************YY*********************Y')
    print('O*********************OO*********************O')
    print('U*********************UU*********************U')
    print('**********************************************')
    print('W*********************WW*********************W')
    print('I*********************II*********************I')
    print('N*********************NN*********************N')
    print('<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>')
    print('<<<<<<<<<<<<<<<<<<<<<---->>>>>>>>>>>>>>>>>>>>>')
    print('<<<<<<<<<<<Thank You For Playing!>>>>>>>>>>>>>')
    print('<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>')
    print('<<<<<<<<<<<<<<<<<<<<<-->>>>>>>>>>>>>>>>>>>>>>>')
if move == 'Exit':
    print("First Chair is a Big Responsibility maybe I should have prepared earlier. Come Back Later.")