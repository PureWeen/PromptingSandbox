"""
Pirate Cat's Treasure Hunt Game
A purr-fectly adventurous game using Python's turtle library!
Control the pirate cat with arrow keys to collect treasures and avoid obstacles!
"""

import turtle
import random
import time
import os
import sys

# Check if we have a display available
def check_display():
    """Check if we can create a turtle graphics window"""
    try:
        # Try to create a test screen
        test_screen = turtle.Screen()
        test_screen.exitonclick()
        return True
    except Exception as e:
        return False

def run_text_version():
    """Run a text-based version of the game when no display is available"""
    print("🐱‍☠️ PIRATE CAT'S TREASURE HUNT - TEXT ADVENTURE! 🐱‍☠️")
    print("=" * 55)
    print("Ahoy matey! No display detected, but fear not!")
    print("Here's a text-based treasure hunting adventure!")
    print()
    
    # Simple text-based game
    treasures_found = 0
    target_treasures = 10
    health = 3
    
    print(f"🎯 Goal: Find {target_treasures} treasures!")
    print(f"❤️  Health: {health} lives")
    print("⚓ Type commands: 'search', 'move', 'status', 'quit'")
    print()
    
    while treasures_found < target_treasures and health > 0:
        print(f"🏴‍☠️ Treasures found: {treasures_found}/{target_treasures} | Lives: {health}")
        action = input("What would ye like to do, captain? ").lower().strip()
        
        if action == 'search':
            if random.random() < 0.6:  # 60% chance of finding treasure
                treasures_found += 1
                print("🏆 Meow-velous! Ye found a treasure chest!")
                if treasures_found == target_treasures:
                    print("🎉 PURR-FECT VICTORY! Ye found all the treasures!")
                    print("Ye be a true pirate cat legend! 🐱‍☠️👑")
                    break
            else:
                if random.random() < 0.3:  # 30% chance of danger
                    health -= 1
                    print("💥 Ouch! A shark attacked! Ye lost a life!")
                    if health == 0:
                        print("💀 Game Over! The sharks got ye, matey!")
                        print(f"Ye found {treasures_found} treasures before meeting Davy Jones!")
                        break
                else:
                    print("🔍 No treasure here, but ye live to search another day!")
        
        elif action == 'move':
            locations = ["mysterious cave", "sandy beach", "rocky cliff", "coral reef", "sunken ship"]
            location = random.choice(locations)
            print(f"🚢 Ye sailed to a {location}!")
            
        elif action == 'status':
            print(f"📊 Status Report:")
            print(f"   🏆 Treasures: {treasures_found}/{target_treasures}")
            print(f"   ❤️  Health: {health}/3")
            print(f"   🎯 Progress: {(treasures_found/target_treasures)*100:.1f}%")
            
        elif action == 'quit':
            print("🏃‍♂️ Ye decided to abandon the treasure hunt!")
            print("Maybe next time, ye scurvy cat! 🐱‍☠️")
            break
            
        else:
            print("❓ Unknown command! Try 'search', 'move', 'status', or 'quit'")
        
        print("-" * 40)
    
    print("\n🐱‍☠️ Thanks for playing Pirate Cat's Treasure Hunt!")
    print("Paws and whiskers! ⚓")

# Set up the screen
try:
    # Add this line to force text mode if desired
    # import sys; sys.exit(run_text_version()) 
    
    screen = turtle.Screen()
    screen.title("🐱‍☠️ Pirate Cat's Treasure Hunt 🏴‍☠️")
    screen.bgcolor("navy")
    screen.setup(width=800, height=600)
    screen.tracer(0)  # Turn off animation for better performance
    HAS_DISPLAY = True
except Exception as e:
    print("🐱‍☠️ Ahoy! No graphical display detected!")
    print("Running text-based adventure instead...")
    print()
    HAS_DISPLAY = False
    run_text_version()
    sys.exit()

# Create the pirate cat (player)
pirate_cat = turtle.Turtle()
pirate_cat.shape("turtle")
pirate_cat.color("orange")
pirate_cat.penup()
pirate_cat.speed(0)
pirate_cat.goto(0, -250)

# Create treasure list
treasures = []
for _ in range(6):
    treasure = turtle.Turtle()
    treasure.shape("circle")
    treasure.color("gold")
    treasure.penup()
    treasure.speed(0)
    treasure.goto(random.randint(-380, 380), random.randint(-200, 280))
    treasures.append(treasure)

# Create obstacles (sharks!)
obstacles = []
for _ in range(4):
    obstacle = turtle.Turtle()
    obstacle.shape("triangle")
    obstacle.color("red")
    obstacle.penup()
    obstacle.speed(0)
    obstacle.goto(random.randint(-380, 380), random.randint(-200, 280))
    obstacles.append(obstacle)

# Score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-390, 260)

# Game variables
score = 0
game_over = False

# Movement functions
def move_up():
    if pirate_cat.ycor() < 280:
        y = pirate_cat.ycor()
        pirate_cat.sety(y + 20)

def move_down():
    if pirate_cat.ycor() > -280:
        y = pirate_cat.ycor()
        pirate_cat.sety(y - 20)

def move_left():
    if pirate_cat.xcor() > -380:
        x = pirate_cat.xcor()
        pirate_cat.setx(x - 20)

def move_right():
    if pirate_cat.xcor() < 380:
        x = pirate_cat.xcor()
        pirate_cat.setx(x + 20)

# Bind keys
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Function to check collision
def is_collision(turtle1, turtle2):
    distance = turtle1.distance(turtle2)
    return distance < 20

# Function to move obstacles randomly
def move_obstacles():
    for obstacle in obstacles:
        x = obstacle.xcor() + random.randint(-5, 5)
        y = obstacle.ycor() + random.randint(-5, 5)
        
        # Keep obstacles within bounds
        if x > 380:
            x = 380
        elif x < -380:
            x = -380
        if y > 280:
            y = 280
        elif y < -280:
            y = -280
            
        obstacle.goto(x, y)

# Function to update score display
def update_score():
    score_display.clear()
    score_display.write(f"Treasures Collected: {score} | Meow-velous! 🐱‍☠️", 
                       align="left", font=("Arial", 16, "bold"))

# Main game loop
def game_loop():
    global score, game_over
    
    while not game_over:
        screen.update()
        
        # Move obstacles
        move_obstacles()
        
        # Check for treasure collection
        for treasure in treasures[:]:  # Use slice to avoid modification during iteration
            if is_collision(pirate_cat, treasure):
                treasure.goto(1000, 1000)  # Move treasure off screen
                treasures.remove(treasure)
                score += 1
                
                # Create new treasure
                new_treasure = turtle.Turtle()
                new_treasure.shape("circle")
                new_treasure.color("gold")
                new_treasure.penup()
                new_treasure.speed(0)
                new_treasure.goto(random.randint(-380, 380), random.randint(-200, 280))
                treasures.append(new_treasure)
        
        # Check for obstacle collision
        for obstacle in obstacles:
            if is_collision(pirate_cat, obstacle):
                game_over = True
                break
        
        # Update score
        update_score()
        
        # Check win condition
        if score >= 15:
            game_over = True
            show_victory()
            break
        
        time.sleep(0.1)
    
    if game_over and score < 15:
        show_game_over()

def show_game_over():
    game_over_text = turtle.Turtle()
    game_over_text.color("red")
    game_over_text.penup()
    game_over_text.hideturtle()
    game_over_text.goto(0, 0)
    game_over_text.write("GAME OVER! 😿\nYe sailed into a shark, matey!\nPress SPACE to play again!", 
                        align="center", font=("Arial", 20, "bold"))
    
    def restart_game():
        screen.clear()
        main()
    
    screen.onkey(restart_game, "space")

def show_victory():
    victory_text = turtle.Turtle()
    victory_text.color("gold")
    victory_text.penup()
    victory_text.hideturtle()
    victory_text.goto(0, 0)
    victory_text.write("PURR-FECT VICTORY! 🏆\nYe collected 15 treasures!\nA true pirate cat legend!\nPress SPACE to play again!", 
                      align="center", font=("Arial", 18, "bold"))
    
    def restart_game():
        screen.clear()
        main()
    
    screen.onkey(restart_game, "space")

def show_instructions():
    # Clear screen and show instructions
    instruction_text = turtle.Turtle()
    instruction_text.color("white")
    instruction_text.penup()
    instruction_text.hideturtle()
    instruction_text.goto(0, 100)
    instruction_text.write("🐱‍☠️ PIRATE CAT'S TREASURE HUNT 🐱‍☠️", 
                          align="center", font=("Arial", 24, "bold"))
    
    instruction_text.goto(0, 50)
    instruction_text.write("Ahoy, me hearty! Welcome aboard!", 
                          align="center", font=("Arial", 16, "normal"))
    
    instruction_text.goto(0, 0)
    instruction_text.write("🗝️ Use ARROW KEYS to move your pirate cat\n🏴‍☠️ Collect golden treasures (circles)\n⚠️ Avoid red sharks (triangles)\n🏆 Collect 15 treasures to win!", 
                          align="center", font=("Arial", 14, "normal"))
    
    instruction_text.goto(0, -100)
    instruction_text.write("Press SPACE to start your adventure!", 
                          align="center", font=("Arial", 16, "bold"))
    
    def start_game():
        screen.clear()
        main()
    
    screen.onkey(start_game, "space")

def main():
    global score, game_over, pirate_cat, treasures, obstacles, score_display
    
    # Reset game variables
    score = 0
    game_over = False
    
    # Set up the screen again
    screen.bgcolor("navy")
    screen.tracer(0)
    
    # Recreate the pirate cat
    pirate_cat = turtle.Turtle()
    pirate_cat.shape("turtle")
    pirate_cat.color("orange")
    pirate_cat.penup()
    pirate_cat.speed(0)
    pirate_cat.goto(0, -250)
    
    # Recreate treasures
    treasures = []
    for _ in range(6):
        treasure = turtle.Turtle()
        treasure.shape("circle")
        treasure.color("gold")
        treasure.penup()
        treasure.speed(0)
        treasure.goto(random.randint(-380, 380), random.randint(-200, 280))
        treasures.append(treasure)
    
    # Recreate obstacles
    obstacles = []
    for _ in range(4):
        obstacle = turtle.Turtle()
        obstacle.shape("triangle")
        obstacle.color("red")
        obstacle.penup()
        obstacle.speed(0)
        obstacle.goto(random.randint(-380, 380), random.randint(-200, 280))
        obstacles.append(obstacle)
    
    # Recreate score display
    score_display = turtle.Turtle()
    score_display.color("white")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(-390, 260)
    
    # Bind keys
    screen.listen()
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    
    # Start the game loop
    game_loop()

# Start with instructions
if __name__ == "__main__":
    if HAS_DISPLAY:
        show_instructions()
        screen.listen()
        screen.exitonclick()
    else:
        # This shouldn't be reached since we exit above, but just in case
        run_text_version()
