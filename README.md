[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/yHBINCbL)
# Django_Forms

Select a project (one of the team members) from the previous sprint and copy the project.

Update POST/PUT methods and templates for adding/editing functionality using Django forms. 


As a result of this sprint (except for the code in the repository) you should get a short video (2-10 minutes) showing
the functionality of the program.




## RUN SMTPD SERVER 
### for using "recovery password"
```
python -m smtpd -n -c DebuggingServer localhost:1025
```

## OUR Mock DB

### How to use
1. Open a terminal and navigate to the directory where mock.py is located.
2. Run the script for update/delete `postgres`  using the following command:
```bash
python mock.py
```
* Use the following arguments to customize the script behavior:
```
-d, --delete_all_data: Deletes all existing product data.
-a, --add_default_data: Adds default product data to the database.
```
