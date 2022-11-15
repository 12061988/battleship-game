# Battleship Game

Portfolio Project 3 Python Essentials - Code Institute


## About

Battleship (also known as Battleships or Sea Battle) is a strategy type guessing game for two players. It is played on ruled grids (paper or board) on which each player's fleet of warships are marked. The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

Battleship is known worldwide as a pencil and paper game which dates from World War I. It was published by various companies as a pad-and-pencil game in the 1930s and was released as a plastic board game by Milton Bradley in 1967. The game has spawned electronic versions, video games, smart device apps and a film.

## How To Play

The game will welcome the user before randomly generating 2 boats locations on the board.
The game will then request that the user enters a column and row number (essentially, co-ordinates) of the location they suspect a battleship is laid. If that location is on a battleship, it is a hit and marked as ‘’o’’. If the location is not on a battleship, it is a miss and marked as ‘’x‘’.
The computer and user will take fifteen turns to find all 2 of the boats, should all 15 turns be taken without finding 2 boats, the game will show "Finished" else "You've Won".
## Features

<img width="821" alt="Capture d’écran 2022-11-15 à 11 25 58" src="https://user-images.githubusercontent.com/107476894/201896178-7c63aea3-0090-470b-a43d-f5a20f19077a.png">




 - The game keeps count of turns and displays this to the user
 - The user must press enter to continue to the next turn to allow them to properly see what is happening at each turn
 - The game is played against the computer
 
## Validators Testing
<img width="1276" alt="Capture d’écran 2022-11-15 à 11 46 52" src="https://user-images.githubusercontent.com/107476894/201901016-4f3c5618-00d6-4234-83c7-a86b3621a2fd.png">


 

## Unfixed Bugs

  - No unfixed bugs
  


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
