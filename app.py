import streamlit as st
import json
import random
from collections import defaultdict



# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Data Science Quiz",
    page_icon="📊",
    layout="centered"
)

# ---------------------------
# Load questions from JSON
# ---------------------------
@st.cache_data
def load_questions(path="questions.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

QUESTIONS = load_questions()

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("🎯 Quiz Settings")

categories = sorted(set(q["category"] for q in QUESTIONS))
difficulties = sorted(set(q["difficulty"] for q in QUESTIONS))

selected_categories = st.sidebar.multiselect(
    "Select Categories",
    categories
   ##default=categories
)

selected_difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    ["All"] + difficulties
)

max_q = len(QUESTIONS)
num_questions = st.sidebar.slider(
    "Number of Questions",
    min_value=1,
    max_value=max_q,
    value=min(5, max_q)
)

start_quiz = st.sidebar.button("🚀 Start Quiz")

# ---------------------------
# Filter questions
# ---------------------------
filtered_questions = [
    q for q in QUESTIONS
    if q["category"] in selected_categories
    and (selected_difficulty == "All" or q["difficulty"] == selected_difficulty)
]

# ---------------------------
# Session State
# ---------------------------
if "feedback" not in st.session_state:
    st.session_state.feedback = None

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "show_summary" not in st.session_state:
    st.session_state.show_summary = False

# ---------------------------
# Start Quiz Logic
# ---------------------------
if start_quiz:
    if len(filtered_questions) == 0:
        st.sidebar.error("No questions match filters")
    else:
        st.session_state.quiz_started = True
        st.session_state.show_summary = False
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.results = []

        # 🔀 Randomize & limit
        random.shuffle(filtered_questions)
        st.session_state.filtered_questions = filtered_questions[:num_questions]

# ---------------------------
# Landing Page
# ---------------------------
if not st.session_state.quiz_started:
    st.title("📊 Data Science Quiz")
    st.write("Choose quiz settings from the sidebar.")
    st.info(f"📌 {len(filtered_questions)} questions available after filters")
    st.stop()

questions = st.session_state.filtered_questions

# ---------------------------
# Score Summary Page
# ---------------------------
if st.session_state.show_summary:
    st.title("🏁 Quiz Results")

    total = len(st.session_state.results)
    score = st.session_state.score
    accuracy = round((score / total) * 100, 2)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Questions", total)
    col2.metric("Correct Answers", score)
    col3.metric("Accuracy", f"{accuracy}%")

    st.markdown("### 📚 Performance by Category")

    category_stats = defaultdict(lambda: {"correct": 0, "total": 0})

    for r in st.session_state.results:
        cat = r["category"]
        category_stats[cat]["total"] += 1
        if r["is_correct"]:
            category_stats[cat]["correct"] += 1

    for cat, stats in category_stats.items():
        st.progress(stats["correct"] / stats["total"])
        st.write(f"**{cat}** — {stats['correct']} / {stats['total']}")

    st.markdown("---")

    if st.button("🔄 Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    st.stop()

# ---------------------------
# Quiz Page
# ---------------------------
q = questions[st.session_state.current_q]

st.title("📊 Data Science Quiz")
st.progress(st.session_state.current_q / len(questions))

with st.container(border=True):
    st.subheader(f"🧠 Question {st.session_state.current_q + 1}")
    st.caption(f"📚 {q['category']} | ⚡ {q['difficulty']}")
    st.markdown(f"**{q['question']}**")

    selected_option = st.radio(
        "Choose your answer:",
        q["options"],
        key=f"q_{st.session_state.current_q}"
    )

# ---------------------------
# Submit Answer
# ---------------------------
if st.button("✅ Submit Answer") and not st.session_state.answered:
    st.session_state.answered = True
    is_correct = selected_option == q["answer"]

    st.session_state.results.append({
        "question": q["question"],
        "category": q["category"],
        "difficulty": q["difficulty"],
        "is_correct": is_correct
    })

    if is_correct:
        st.session_state.score += 1
        st.session_state.feedback = ("success", "Correct 🎉")
    else:
        st.session_state.feedback = (
            "error",
            f"Wrong ❌  \n**Correct:** {q['answer']}"
        )

if st.session_state.feedback:
    kind, message = st.session_state.feedback
    if kind == "success":
        st.success(message)
    else:
        st.error(message)

# ---------------------------
# Next Question
# ---------------------------
if st.session_state.answered:
    if st.button("➡️ Next"):
        st.session_state.current_q += 1
        st.session_state.answered = False
        st.session_state.feedback = None  # 👈 clear message

        if st.session_state.current_q >= len(questions):
            st.session_state.show_summary = True
            st.rerun()
