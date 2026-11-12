import sqlite3

DATABASE_NAME = "quiz_questions.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            answer TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM questions")

    if cursor.fetchone()[0] == 0:
        sample_questions = [
            ("Which data structure uses FIFO?",
             "Stack", "Queue", "Tree", "Graph", "B", "Easy", 1),

            ("Which algorithm works on sorted arrays?",
             "Linear Search", "Binary Search", "Bubble Sort", "DFS", "B", "Easy", 1),

            ("What is the time complexity of Merge Sort?",
             "O(n)", "O(n log n)", "O(n²)", "O(log n)", "B", "Medium", 2),

            ("Which data structure follows LIFO?",
             "Queue", "Stack", "Array", "Graph", "B", "Easy", 1),

            ("Which sorting algorithm selects the minimum element?",
             "Bubble Sort", "Merge Sort", "Selection Sort", "Quick Sort", "C", "Medium", 2)
        ]

        cursor.executemany("""
            INSERT INTO questions
            (question, option_a, option_b, option_c, option_d,
             answer, difficulty, marks)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, sample_questions)

    connection.commit()
    connection.close()


def get_all_questions():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM questions ORDER BY id DESC")
    questions = [dict(row) for row in cursor.fetchall()]

    connection.close()
    return questions


def add_question(data):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO questions
        (question, option_a, option_b, option_c, option_d,
         answer, difficulty, marks)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["question"],
        data["option_a"],
        data["option_b"],
        data["option_c"],
        data["option_d"],
        data["answer"],
        data["difficulty"],
        data["marks"]
    ))

    connection.commit()
    connection.close()


def delete_question(question_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM questions WHERE id = ?",
        (question_id,)
    )

    connection.commit()
    connection.close()