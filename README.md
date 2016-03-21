## Synopsis

## Installation

Below you can find instruction to install and run the application on your local machine

Run the following command to clone the repository in a local directory:
git clone https://github.com/npitsillos/WAD-EHealth.git

The requirements.txt file contains all the necessary packages for the application to run.
To install requirements, run in the command prompt:
pip install -r requirements.txt

Navigate to ehealthexplorer directory and execute the following command to run the population script:
python populate_explorer.py

Run the django server:
manage.py runserver

Navigate to home page:
http://127.0.0.1/explorer/

## Population Script

Inside the root directory of the application there is a population script which populates some dummy data into the application for demonstration purposes.
Below there are details about the data populated.

Here is a list of the users created:
Username		Email			Password
jill			jill@jill.com	jill
bob				bob@bob.com		bob
joe				joe@joe.com		joe

Jill:
Jill has one category called 'Flu' which is shared and contains two pages.

Bob:
Bob has two categories called 'Cancer' and 'Sclerosis'. Both of them contain two pages and 'Sclerosis' is shared.

Joe:
Joe has one category called Diabetes and contains two pages.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.
