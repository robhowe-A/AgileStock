# AgileStock

CSC480A - AgileStock inventory management application

### NOTE: Before cloning the repro, be sure to have git installed  
- Windows: GitForWindows is a good installer. It adds terminal to right-click options as a plus!  
  ```
  https://gitforwindows.org/
  ```
  
- Linux: use the terminal command, like below, for your OS.  
  ``` Bash
  # apt-get install git
  ```

## Development Environment

1. Clone the repro to a local folder
   ```
   git clone https://github.com/robhowe-A/AgileStock.git
   ```
2. Start the web server
   ```
   py -m runserver
   ```

### Dependencies

- This project runs with Python, be sure have Python 3.11 installed on the server.  
- MySQL installed on the same computer as the project runtime. Currently, the project is specific to MY installation. The username, password, and database are all hard coded in the project.  
- It requires Flask, however, a yml workflow is set up to do the dependency install automatically (unconfirmed by team members).  

```
py -m pip install Flask
```
