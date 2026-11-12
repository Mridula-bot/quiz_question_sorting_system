# Quiz Question Sorting System

A web-based Quiz Question Sorting System built with **Python, Flask, and
SQLite**. The project is designed to organize quiz questions so they can
be managed and sorted through a simple web application.

> **Project note:** This README is based on the supplied Makefile and
> the project title. Update the feature list and usage instructions if
> your application has specific sorting options, categories, difficulty
> levels, or question formats.

## Objectives

-   Organize quiz questions in one place.
-   Make quiz questions easier to find and manage.
-   Provide a simple web interface for working with quiz questions.
-   Store question data in an SQLite database.

## Technologies Used

-   **Python 3** --- backend programming
-   **Flask** --- web application framework
-   **SQLite** --- database
-   **HTML/CSS** --- interface (if used in the project)

## Project Structure

``` text
quiz-question-sorting-system/
├── app.py             # Main Flask application
├── database.py        # Database initialization
├── Makefile           # Setup and run commands
├── quiz_questions.db  # SQLite database (created during setup)
├── templates/         # HTML templates, if used
└── static/            # CSS, JavaScript, and other assets, if used
```

## Requirements

-   Python 3
-   Make
-   A web browser

## Installation and Setup

Open Terminal in the project folder and run these commands.

### 1. Create a virtual environment

``` bash
make venv
```

### 2. Install dependencies

``` bash
make install
```

This installs Flask in the project's virtual environment.

### 3. Initialize the database

``` bash
make db
```

### 4. Run the application

``` bash
make run
```

Open the local URL shown in the terminal in your web browser. Flask
commonly uses:

``` text
http://127.0.0.1:5000
```

Keep the terminal open while using the application.

## Makefile Commands

  -----------------------------------------------------------------------
  Command                             Purpose
  ----------------------------------- -----------------------------------
  `make help`                         Shows the available commands

  `make venv`                         Creates the Python virtual
                                      environment

  `make install`                      Installs or upgrades pip and
                                      installs Flask

  `make db`                           Initializes the SQLite database

  `make run`                          Starts the Flask application

  `make reset`                        Deletes and recreates
                                      `quiz_questions.db`

  `make clean`                        Removes the virtual environment and
                                      Python cache files
  -----------------------------------------------------------------------

**Important:** `make reset` deletes the existing `quiz_questions.db`
file. Back up any questions or data you want to keep before running it.

## How to Use

1.  Start the project with `make run`.
2.  Open the local Flask address in your browser.
3.  Use the options provided on the application pages to work with quiz
    questions.
4.  Apply the sorting or organization options available in the
    application.
5.  Review the displayed questions.

The exact sorting criteria and available actions depend on the
implementation in `app.py`.

## Database

The project uses SQLite. The Makefile initializes the database by
calling the `initialize_database()` function from `database.py`.

The database file used by the Makefile is:

``` text
quiz_questions.db
```

## Troubleshooting

-   **`make: command not found`** --- install Make, or run the
    equivalent Python commands manually.
-   **`python3: command not found`** --- install Python 3 and ensure it
    is available in your terminal.
-   **Flask module not found** --- run `make install` from the project
    directory.
-   **Database initialization error** --- check that `database.py`
    contains the `initialize_database()` function.
-   **Application does not start** --- check that `app.py` exists in the
    project directory and review the error shown in Terminal.

## Future Scope

Possible improvements include:

-   Sorting questions by subject or topic
-   Filtering by difficulty level
-   Searching questions by keywords
-   Supporting multiple-choice and other question formats
-   Adding, editing, and deleting questions
-   Generating quizzes from selected questions

These are suggested enhancements; include them as current features only
if they are implemented.

## Author

**Name:** Add your name\
**Course:** Add your course\
**Institution:** Add your institution
