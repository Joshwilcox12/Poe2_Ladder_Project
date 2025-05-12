This project was started because I want to learn what getting data from one source to another is like as
I would like to learn more about data engineering.
What I hope to learn from this project is python, api, automating systems, more advanced sql, and pipelines.

I am using chatgpt to help on this project, though I feel I may be relying on it too much and would like to use it less and less through the project.
In future projects I would like to use it less, or at least non of the code it gives me.


Flow of the project so far is: 
1) I use POE2_Ladder.py to grab the top 1000 players on the hc ladder.
2) I upload that data into a csv file, and upload it to my sql database.
3) This script is ran daily at noon.
4) I then use the csv file I downloaded to input the top 100 players and run the script
Grab_Trade.py. This script will take each player and use the trade api to get their item listings
in the format I want.

