This project contains a flaskproject folder which contains the main HTML Page DublinBikes in /templates, 
the accompanying static JSON and CSS files in /static as well as a queries.py and app.py scripts that run the website using flask and query a remote database.

The setup.py file was designed for the scraping programs contained in the src package. 
In src, main.py is the main scraping script. This was run on a different git repository, but is included with these files.
rds_config contains the login information for RDS database and connecting to the ec2 instance. The other files in src are all various tests.