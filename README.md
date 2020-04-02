# Utilities Dashboard Repo

This repo serves to remotely store the Django stack for a dashboard designed to facilitate utilities expense tracking for my roomates and I, as well as other features to facilitate household expense accounting.

**Dashboard Description**

The utilities dashboard is meant to serve all needs in recording utilities expenses as well as grocery bills. The dashboard is built over an SQLite database.

The dashboard will eventually offer an additional feature to facilitate the retrieval of grocery lists for orders through Amazon PrimeNow/Fresh (given a set of user login information) as well as a prediction algorithm for sorting the items among individuals involved in the order. The prediction alogorithm will rely on a set of previously ordered grocery data to make new predictions.

**Run the dashboard locally**

To open a local session and use the dashboard through your browser, follow these steps:

*Mac OS*

1) Download the directories *house_dashboard* and *myvenv*.
2) In the terminal, cd to the directory containing the two downloaded subdirectories.
3) Run the following commands:

	$ source myvenv/bin/activate

	$ cd house_dashboard

	$ python manage.py runserver

4) If the dashboard has activateed properly, you should see a line in the terminal similar to: 'Starting development server at http://127.0.0.1:8000/'
5) Copy and paste the 'http' link from the terminal into your browser url to open the dashboard.

*Linux (Ubuntu 18.04)*

1) Download the directories *house_dashboard* and *myvenv*.
2) In the terminal, cd to the directory containing the two downloaded subdirectories.
3) Run the following commands:

        $ source myvenv/bin/activate

        $ cd house_dashboard

        $ python3 manage.py runserver

4) If the dashboard has activateed properly, you should see a line in the terminal similar to: 'Starting development server at http://127.0$
5) Copy and paste the 'http' link from the terminal into your browser url to open the dashboard.

**Deactivate the Dashboard**

1) To end the session, type 'Control + C' into the terminal running the server.
2) To deactivate the virtual environment and return to base, type 'deactivate'.

#### Note on the virtual environment supporting the project

The virtual env. 'myvenv' is constructed to contain all dependencies for the stack. However, it may contain spurious packages imported during experimentation while building features to be added to the dashboard. In the final product, these spurious python packages will need to be removed.
