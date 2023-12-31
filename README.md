# AgileStock

CSC480A - AgileStock inventory management application

### NOTE: Before cloning the repro, be sure to have git installed

- Windows: GitForWindows is a good installer. It adds terminal to right-click options as a plus!
  ```
  https://gitforwindows.org/
  ```
- Linux: use the terminal command, like below, for your OS.
  ```Bash
  # apt-get install git
  ```

## Development Environment

1. Clone the repro to a local folder
   ```
   git clone https://github.com/robhowe-A/AgileStock.git
   ```
2. Start the web server
   ```
   py -m app
   ```

### Dependencies

#### Python: Flask + PyMySQL

- This project runs with Python, be sure have Python 3.11 installed on the server.
- MySQL installed on the same computer as the project runtime. Currently, the project is specific to MY installation. The username, password, and database are all hard coded in the project.
- It requires Flask and PyMySQL, however, a yml workflow is set up to do the dependency install automatically (unconfirmed workflow).

```
py -m pip install Flask
py -m pip install PyMySQL
```

#### Database: MySQL database

- At the project's runtime connects to MySQL database with (below) parameters. You'll need MySQL installed on the same computer. Then, change the code variables to your database instance parameters for username, password, database name. Host should be localhost if on the same computer:

```Python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '<root's password>'
app.config['MYSQL_DB'] = '<database name>'
```

- MySQL Database
  > MySQL Server (Full) - community (mysql-installer-community-8.0.35.0.msi)  
  > MySQL Workbench (requires C++ Redistributable installation)  
  > Download link: https://dev.mysql.com/downloads/installer/ (mysql-installer-community-8.0.35.0.msi)
