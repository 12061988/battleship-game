# Battleship Game

Portfolio Project 3 Python Essentials - Code Institute


## About

Battleship (also known as Battleships or Sea Battle[1]) is a strategy type guessing game for two players. It is played on ruled grids (paper or board) on which each player's fleet of warships are marked. The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

Battleship is known worldwide as a pencil and paper game which dates from World War I. It was published by various companies as a pad-and-pencil game in the 1930s and was released as a plastic board game by Milton Bradley in 1967. The game has spawned electronic versions, video games, smart device apps and a film.

## How To Play

The game will welcome the user before randomly generating 5 ships locations on the board.
The game will then request that the user enters a column and row number (essentially, co-ordinates) of the location they suspect a battleship is laid. If that location is on a battleship, it is a hit and marked as ‘’X’’. If the location is not on a battleship, it is a miss and marked as ‘’ - ‘’.
The computer and user will take fifteen turns to find all 5 of the ships, should all 15 turns be taken without finding 5 ships, the game will state who has had the most hits and display them as the winner.

## Features

<img width="828" alt="Capture d’écran 2022-08-06 à 10 35 22" src="https://user-images.githubusercontent.com/107476894/183241591-11fce2c4-f0b9-4ed2-a33c-21afc7389f23.png">


## Existing Features

 - The game keeps count of turns and displays this to the user
 - The user must press enter to continue to the next turn to allow them to properly see what is happening at each turn
 - The game is played against the computer

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

The steps for deployment are as follows:

 - Fork or clone this repository
 - Create a new Heroku app
 - Set the buildpacks to Python and NodeJS in that order
 - Link the Heroku app to the repository
 - Click on Deploy


## Credits

This project uses the Code Institute student template for deploying the third portfolio project, the Python command-line project.
The idea of using battleships is a suggested one by the Code Institute and as inspiration Youtube tutorials adapted to my own vision.
