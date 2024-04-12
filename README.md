# COMP 3005 Final Project
# https://github.com/statsbomb/open-data/tree/0067cae166a56aa80b2ef18f61e16158d6a7359a

> < python3 json_loader/loader.py > to initialize the database

Instructions:

Initiating the database.
    In PGadmin4, creat a database called: comp3005finalproject
    Open dbInit.py and change the password variable on line 3 to the password encrypting the root "postgress" user on your machine
    Run dbInit.py








Announcements from brightspace:

Mar 21, 2024:
Hi Project 1 folks,

I would like to share some good news with you regarding project 1:

Part of the source code of the auto-grader is now publicly available for you to access and try out. This can be found here.
You are no longer required to write the code to execute your query and write the results into files. The "queries.py" file in the above GitHub repository does this for you. You're only required to insert your SQL queries in the right places in that file. The auto-grader takes care of the rest. Just make sure that you carefully read the documentation of the auto-grader and do NOT change anything else in the file other than the queries before you submit your work.
I uploaded a new version of the problem statement that reflects these changes and clarifies what is required in the queries. So, please have another look at the problem statement.
If you find any issues with the "queries.py" code, please read the documentation to know how to report them to the TA responsible for coding the auto-grader. 

Please let me know if you have any further question by posting on the discussion forum of the project. 

-Ahmed


Mar 22, 2024
Hi again,

I noticed that this question was asked a couple of times to me during office hours and on the forum. So, I should clear things out.

The question is: Can we just create our schema and load our database with the data that involves only the attributes in the problem statement (in the 10 queries)?

Answer: Absolutely not. In fact, this will be considered cheating. The reason is that if you only use these attributes, your schema is much simpler, and your database is much smaller. This means that your queries will definitely execute faster than a more decent solution that loads data from all the attributes. 

What you need to load in your database: Almost everything from the four seasons in the problem statement (La Liga 2020/2021, 2019/2020, 2018/2019, and Premier League 2003/2004). This includes data from competitions.json, the files from these seasons in the directories "matches", "lineups", and "events". Some attributes aren't relevant to the objective of the project, which is running aggregate queries that may result in some interesting facts similar to the 10 queries in the problem statement. Here are some examples to give you a better idea:

In the "matches" directory, for any of the matches files, attributes like "match_status" : "available", "match_status_360", "last_updated", "last_updated_360", "metadata", "data_version", "shot_fidelity_version", "xy_fidelity_version" are probably used internally at Statsbomb as metadata. This is irrelevant to data about the game. So, not needed. On the other hand, attributes that aren't in the problem statement but exist in the file like "match_week", "referee", "stadium", "home_team", etc, although not in the problem statement, they should be in your database.
In the "events" directory, for any of the events files, an attribute like "related_events" may be considered relevant or not. But almost every other attribute is important and should be in your database.
In the "competitions.json" file, again, attributes like "match_updated", "match_updated_360", "match_available_360", and "match_available" are metadata attributes and won't be relevant. 
You get the idea by now. So, please try to be exhaustive in your mapping of the dataset into your database.

What else is considered cheating: Creating materialized views for the queries in the problem statement. Why? Because again, your design should be used to answer any aggregate queries. If you create materialized views only for the queries in the problem statement but nothing else, your database is going to be good only in these queries.

What is not considered cheating: Table partitioning, and use of indexes.

Hope this helps you better understand the problem. 

-Ahmed



Mar 25, 2024
Hi everyone,

I would like to clarify one thing about the queries in the problem statement: In all the queries, we rely on straight-forward counting. Nothing that is more complicated. For example, consider the first query asking about the average xG scores of players. This implies that we're considering only the players that made at least one shot. That is, players who never made a shot will never have an associated xG score. The right way of going about this would be to check the lineup to see whether a player starts in a game or gets substituted without making a shot, or simply output all the players who do not have an xG value associated with them with a value 0. We're not interested in these special cases. The same applies to the rest of the queries.

I updated the project file with more details for every query and re-uploaded it.

Best,

-Ahmed
