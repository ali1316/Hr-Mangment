# HR Management Project

This project is a Human Resources (HR) Management application built with Angular and Django Restful API. It allows HR managers to perform various actions related to managing branches and employees.

## Features

### Manage Branches

- View all branches in the system, including branch details.
- Create new branches and update existing ones.
- Delete branches from the system.
- Branches have fields such as name, building number, street, area, city, country, and an optional manager field.
- Managers can be selected from a dropdown list of employees assigned to that branch.
- Viewing branch details displays a list of all employees assigned to that branch.
- Deleting a branch also removes all employees assigned to it.

### Manage Employees

- View all employees in the system, including employee details.
- Create new employees and update existing ones.
- Delete employees from the system.
- Employees have fields such as name, age, email, phone number, and branch.
- The branch field is selected from a drop-down list of all branches.
- Deleting an employee who is the manager of a branch does not assign a new manager to that branch.

## Technologies Used

- Angular
- Django Restful API
- Bootstrap
- MySQL

## Project Setup

### Django Backend

1. **Install required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Configure the database connection in `HRManagement/settings.py`.**

3. **Run migrations to create database tables:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

### Angular Frontend

1. **Install Angular CLI:**

    ```bash
    npm install -g @angular/cli
    ```

2. **Install project dependencies:**

    ```bash
    npm install
    ```

3. **Start the Angular development server:**

    ```bash
    ng serve
    ```

4. **Open the application in your browser: [http://localhost:4200/](http://localhost:4200/)**

## Usage

Navigate to the HR Management application, view and manage branches and employees, and enjoy the user-friendly interface for HR tasks.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.
