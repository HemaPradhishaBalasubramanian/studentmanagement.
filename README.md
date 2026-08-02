
# Student Management System

A desktop-based Student Management System developed using Python, Tkinter, and MySQL. I built this application to simplify how student records are handled. Managing student information manually can be tedious and prone to errors, so this project automates the process. It features an intuitive graphical interface where users can easily perform CRUD (Create, Read, Update, Delete) operations while keeping data securely stored in a MySQL database.

## Features
- Add new student records to the database
- Update existing student details when information changes
- Delete student records that are no longer needed
- Search for specific students by ID or name
- View a comprehensive list of all student records
- Secure data storage powered by MySQL
- An easy-to-use, intuitive Tkinter GUI
- Built-in input validation and error handling to prevent bad data

## Technologies Used
- Python
- Tkinter (for the GUI)
- MySQL
- SQL

## Project Structure
```text
Student-Management-System/
|-- database/
|   |-- student_db.sql
|
|-- images/
|
|-- src/
|   |-- main.py
|   |-- database.py
|   |-- student.py
|   |-- utils.py
|
|-- requirements.txt
|-- README.md
```

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/Student-Management-System.git
```

2. **Navigate to the project folder**
```bash
cd Student-Management-System
```

3. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up the MySQL Database**
- Open your MySQL client.
- Create a new database named:
```sql
CREATE DATABASE student_db;
```
- Import the provided SQL file (`database/student_db.sql`) if available.

5. **Update Database Credentials**
Open `src/database.py` (or your main configuration file) and update the connection variables to match your local MySQL setup:
```python
host = "localhost"
user = "root"
password = "your_password"
database = "student_db"
```

6. **Run the application**
```bash
python src/main.py
```

## How It Works
1. Launch the application to open the desktop interface.
2. Fill out the form with the student's details.
3. Click Save to securely store the record in the MySQL database.
4. Use the search bar to find specific students, or select a record to update or delete it.
5. View all saved student information directly within the application window.

## Learning Outcomes
Building this project was a great hands-on learning experience. Along the way, I improved my skills in:
- Building desktop GUI applications using Tkinter.
- Implementing full CRUD operations.
- Connecting Python to a MySQL database.
- Writing and executing SQL queries.
- Handling exceptions and validating user input.
- Structuring an application and managing a relational database.

## Future Enhancements
As I continue to develop this project, I plan to add:
- A login system for user authentication.
- An attendance tracking module.
- The ability to upload and store student photos.
- A feature to export records to Excel or PDF.
- An analytics dashboard to visualize student data.
- Cloud database integration so the app can be accessed remotely.

## Screenshots
*(Add screenshots of your Home Screen, Registration Form, Records Table, and Search Function here)*

## Contributing
Contributions, suggestions, and feedback are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## Author
**Hema Pradhisha Balasubramanian**
- GitHub: https://github.com/HemaPradhishaBalasubramanian
```
