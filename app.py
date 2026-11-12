from flask import Flask, render_template, request, redirect, url_for
from database import (
    initialize_database,
    get_all_questions,
    add_question,
    delete_question
)
from algorithms import (
    bubble_sort,
    selection_sort,
    merge_sort,
    linear_search,
    binary_search
)

app = Flask(__name__)

initialize_database()


@app.route("/")
def home():
    questions = get_all_questions()

    search_text = request.args.get("search", "").strip()
    search_method = request.args.get("search_method", "linear")
    sort_method = request.args.get("sort_method", "none")
    sort_key = request.args.get("sort_key", "question")

    found_question = None

    if search_text:
        if search_method == "binary":
            found_question = binary_search(questions, search_text)
            questions = [found_question] if found_question else []
        else:
            found_question = linear_search(questions, search_text)
            questions = [
                q for q in questions
                if search_text.lower() in q["question"].lower()
            ]

    if sort_method == "bubble":
        questions = bubble_sort(questions, sort_key)
    elif sort_method == "selection":
        questions = selection_sort(questions, sort_key)
    elif sort_method == "merge":
        questions = merge_sort(questions, sort_key)

    return render_template(
        "index.html",
        questions=questions,
        search_text=search_text,
        search_method=search_method,
        sort_method=sort_method,
        sort_key=sort_key,
        found_question=found_question
    )


@app.route("/add", methods=["POST"])
def add():
    data = {
        "question": request.form["question"].strip(),
        "option_a": request.form["option_a"].strip(),
        "option_b": request.form["option_b"].strip(),
        "option_c": request.form["option_c"].strip(),
        "option_d": request.form["option_d"].strip(),
        "answer": request.form["answer"],
        "difficulty": request.form["difficulty"],
        "marks": int(request.form["marks"])
    }

    if all(data[key] for key in [
        "question", "option_a", "option_b",
        "option_c", "option_d"
    ]):
        add_question(data)

    return redirect(url_for("home"))


@app.route("/delete/<int:question_id>", methods=["POST"])
def delete(question_id):
    delete_question(question_id)
    return redirect(url_for("home"))


@app.route("/quiz")
def quiz():
    questions = get_all_questions()
    return render_template("quiz.html", questions=questions)


@app.route("/submit-quiz", methods=["POST"])
def submit_quiz():
    questions = get_all_questions()

    score = 0
    total = len(questions)
    results = []

    for question in questions:
        selected = request.form.get(str(question["id"]), "")
        correct = selected == question["answer"]

        if correct:
            score += question["marks"]

        results.append({
            "question": question["question"],
            "selected": selected if selected else "Not Attempted",
            "correct_answer": question["answer"],
            "correct": correct
        })

    return render_template(
        "result.html",
        score=score,
        total=total,
        results=results
    )


if __name__ == "__main__":
   app.run(debug=True, port=5001)