# E-Library

Website that allows users to reserve books online, and librarians to manage all books, users and reservations in the library.

### Technologies

Technologies used on the frontend of the application are the basic web technologies (HTML, CSS, JS). Backend of the application was built in Python, specifically Flask. MySQL is used for storing data.

### Setup

Sofware you need for running this project locally are Python and some software for running MySQL database (XAMPP, WAMP...). The following commands work for Windows, if you use some other OS find the alternative to these commands. Clone the repository and make sure you are located in the project root folder.

1. You need to create python virtual enviroment with the following command:

- python -m venv env

2. Then you need to activate it:

- env\Scripts\activate

3. Installing packages (flask, flask_mysqldb):

- pip install -r requirements.txt

If you can't install from `reqirements.txt` file you can install the manually:

- pip install flask, flask_mysqldb

4. Make new MySQL database called "biblioteka" (if you want to name it differently you can edit the source code), then import the database schema from `biblioteka.sql` file

5. If everything went okay, you can run the server by executing `app.py` file

### Contributors

1. Balsa Dogandzic, [GitHub](https://github.com/Balsa-Dogandzic)
2. Josif Vukicevic, [GitHub](https://github.com/JosifVukicevic)
