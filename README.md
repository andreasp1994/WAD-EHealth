# Synopsis

Web Application Development Course - Group Project

The purpose of this application is to help people find out about particular conditions and to save the information that they find into different folders. The application lets people search across two different medical sites (medline and healthfinder) and the general web (bing).
People using the application can self-diagnose, i.e. given some symptoms find out what are the likely conditions. They can also like to find out information about particular conditions, treatments and medicines. The application helps the users understand if the information is easy to read, is loaded with senitment and subjectivity.

The API’s for the federated search are:

http://healthfinder.gov/developer/How_to_Use.aspx <br />
https://www.nlm.nih.gov/medlineplus/webservices.html <br />
https://datamarket.azure.com/dataset/bing/search <br />

# Installation

Below you can find instruction to install and run the application on your local machine

Run the following command to clone the repository in a local directory:
<br />
git clone https://github.com/npitsillos/WAD-EHealth.git

The requirements.txt file contains all the necessary packages for the application to run.
To install requirements, run in the command prompt:
<br />
pip install -r requirements.txt

Navigate to ehealthexplorer directory and execute the following command to run the population script:
<br />
python populate_explorer.py

Run the django server
<br />
manage.py runserver

Navigate to home page:
<br />
http://127.0.0.1/explorer/

NOTE: Keys are required for Bing and HealthFinder, app is set up to read from keys.py file in the explorer folder

# Population Script

Inside the root directory of the application there is a population script which populates some dummy data into the application for demonstration purposes.
Below there are details about the data populated.

Here is a list of the users created: <br />
Username: jill
Email: jill@jill.com
Password: jill

Username: bob
Email: bob@bob.com
Password: bob

Username: joe
Email: joe@joe.com
Password: joe

Jill:
Jill has one category called 'Flu' which is shared and contains two pages.

Bob:
Bob has two categories called 'Cancer' and 'Sclerosis'. Both of them contain two pages and 'Sclerosis' is shared.

Joe:
Joe has one category called Diabetes and contains two pages.

# Contributors

2079310R: Emily Raine, 2079310R

npitsillos: Nikolas Pitsillos, 2126280P 

andreasp1994: Antreas Pogiatzis, 2140845P

OrlinODachev: Orlin Dachev, 2131228D 

# Bugs and Fixes

###24.03.2016 - Bug: 
Some topics cannot be saved in the user defined categories.
###update: 
Problem fixed. There was a bug in the save-to.js file and to results.html template. 
Save functionality now works properly.



