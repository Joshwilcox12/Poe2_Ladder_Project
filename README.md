This project was started because I want to learn what getting data from one source to another is like.
I want to learn more about data engineering.
What I hope to learn from this project is python, api, automating systems, more advanced sql, and pipelines.

Flow of the project so far is: 
1) I use POE2_Ladder.py to grab the top 1000 players on the hc ladder.
2) I upload that data into a csv file, then upload it to my sql database.
3) This script is ran daily at noon.
4) I then use the csv file I downloaded to input the top 100 players and run the script
Grab_Trade.py. This script will take each player and use the trade api to get their item listings
in the format I want.

I have learned to navigate public api using inspect.
Using python to grab specific data I want from a REST api.
Transforming json to csv using python.
cleaning data, such as removing characters in strings, nested dictionary, loops to grab values I want and creat now key value pairs or list.
Putting sleep so api does not hit rate limit.
Creating tables in pgadmin.
Uploading data from csv or directly from python to database.
Locally using task scheduler to automate the task.


Things I would love to do in future for this project:

remove data past more than 2 weeks old, I'm running into storage issues.
move this data to some sort of cloud.
run this task without it being limited to local computer.
create sql quries/tasks that can answer questions that a client would want, either internal or external.
Using the query created above to load the data into some sort of visual tool.

