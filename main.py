import pygame as pg
import math
from obj import Hand, Agent

def reset_background(background):
    background.fill((0, 0, 0))

    # Calculate the center coordinates
    center = (background.get_width()/2,background.get_height()/2)

    # Put the hour marks
    for angle in [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]:
        tick_length = 375
        tick_width = 5
        x = center[0] + math.cos(math.radians(angle)) * tick_length
        y = center[1] + math.sin(math.radians(angle)) * tick_length
        # then render the line center->(x,y)
        pg.draw.line(background, (255, 255, 255), center, (x,y), tick_width)
    # Cover center with black circle
    pg.draw.circle(background, (0,0,0), center, 350)

def main():
    # Initialize Everything
    pg.init()
    screen = pg.display.set_mode((800, 800), pg.SCALED)
    pg.display.set_caption("Clockwerk")

    # Create The Background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    reset_background(background)


    # Put Minute Hand on Background
    hand_length = 300
    minute_hand = Hand(background, hand_length, 10, (255, 255, 255))

    # Put hour hand
    hand_length = 150
    hour_hand = Hand(background, hand_length, 20, (255, 255, 255))

    # Put agents
    agents = []
    for i in range(10):
        agent = Agent(background, i)
        agents.append(agent)
    
    # Display The Background
    screen.blit(background, (0, 0))
    pg.display.flip()

    clock = pg.time.Clock()

    # Main Loop
    while True:
        clock.tick(60)
        reset_background(background)

        for event in pg.event.get():
            pass
        # process events

        minute_hand.update()
        hour_hand.update()
        for agent in agents:
            agent.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        pg.display.flip()

    pg.quit()


# Game Over


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()