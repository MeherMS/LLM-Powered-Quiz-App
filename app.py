import random
import streamlit as st
import pandas as pd

from questions import QUESTIONS
from leaderboard import load_leaderboard, save_score, clear_leaderboard

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="DS & AI Quiz",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────
# CUSTOM CSS
# ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

/* ── Background ── */
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #141432 50%, #0f0c29 100%);
    min-height: 100vh;
}

/* ── Main container ── */
.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* ── Headings ── */
h1 { color: #e2e8f0 !important; font-weight: 700 !important; letter-spacing: -0.5px; }
h2 { color: #cbd5e1 !important; font-weight: 600 !important; }
h3 { color: #94a3b8 !important; font-weight: 500 !important; }

/* ── Hero card ── */
.hero-card {
    background: linear-gradient(135deg, rgba(99,102,241,0.15) 0%, rgba(139,92,246,0.1) 100%);
    border: 1px solid rgba(99,102,241,0.3);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-bottom: 2rem;
    backdrop-filter: blur(10px);
}

.hero-title {
    font-size: 2.6rem;
    font-weight: 700;
    background: linear-gradient(90deg, #818cf8, #c084fc, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
    margin-bottom: 0.5rem;
}

.hero-subtitle {
    color: #94a3b8;
    font-size: 1.05rem;
    margin-top: 0.5rem;
}

/* ── Question card ── */
.question-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 1.8rem 1.8rem 1.4rem;
    margin-bottom: 1.2rem;
}

.question-meta {
    display: flex;
    gap: 0.6rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
}

.badge {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-family: 'JetBrains Mono', monospace;
}

.badge-cat  { background: rgba(99,102,241,0.2);  color: #818cf8; border: 1px solid rgba(99,102,241,0.4); }
.badge-easy { background: rgba(34,197,94,0.2);   color: #4ade80; border: 1px solid rgba(34,197,94,0.4); }
.badge-med  { background: rgba(251,191,36,0.2);  color: #fbbf24; border: 1px solid rgba(251,191,36,0.4); }
.badge-hard { background: rgba(239,68,68,0.2);   color: #f87171; border: 1px solid rgba(239,68,68,0.4); }

.question-text {
    color: #e2e8f0;
    font-size: 1.15rem;
    font-weight: 500;
    line-height: 1.6;
    margin: 0;
}

/* ── Answer feedback ── */
.feedback-correct {
    background: rgba(34,197,94,0.12);
    border: 1px solid rgba(34,197,94,0.4);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    color: #4ade80;
    font-weight: 500;
    margin-top: 0.8rem;
}

.feedback-wrong {
    background: rgba(239,68,68,0.12);
    border: 1px solid rgba(239,68,68,0.4);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    color: #f87171;
    font-weight: 500;
    margin-top: 0.8rem;
}

.explanation-box {
    background: rgba(56,189,248,0.08);
    border: 1px solid rgba(56,189,248,0.25);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    color: #7dd3fc;
    font-size: 0.92rem;
    line-height: 1.6;
    margin-top: 0.8rem;
}

/* ── Progress bar ── */
.progress-container {
    background: rgba(255,255,255,0.07);
    border-radius: 999px;
    height: 8px;
    overflow: hidden;
    margin-bottom: 0.4rem;
}

.progress-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #818cf8, #c084fc);
    transition: width 0.4s ease;
}

/* ── Score card ── */
.score-card {
    background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(139,92,246,0.15));
    border: 1px solid rgba(139,92,246,0.4);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
}

.score-number {
    font-size: 4rem;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    background: linear-gradient(90deg, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.score-label {
    color: #94a3b8;
    font-size: 1rem;
    margin-top: 0.3rem;
}

/* ── Leaderboard ── */
.lb-header {
    font-size: 1.5rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.lb-row {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 0.75rem 1.2rem;
    margin-bottom: 0.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.lb-rank { font-family: 'JetBrains Mono', monospace; color: #c084fc; font-weight: 600; font-size: 0.95rem; }
.lb-name { color: #e2e8f0; font-weight: 500; }
.lb-pct  { font-family: 'JetBrains Mono', monospace; color: #4ade80; font-weight: 600; }

/* ── Streamlit overrides ── */
.stRadio > div { gap: 0.5rem !important; }

.stRadio label {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 10px !important;
    padding: 0.75rem 1rem !important;
    color: #cbd5e1 !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    font-size: 0.95rem !important;
}

.stRadio label:hover {
    background: rgba(99,102,241,0.15) !important;
    border-color: rgba(99,102,241,0.5) !important;
    color: #e2e8f0 !important;
}

div[data-testid="stRadio"] p { color: #e2e8f0 !important; }

.stButton > button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.65rem 2rem !important;
    font-weight: 600 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.3px !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 15px rgba(99,102,241,0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(99,102,241,0.5) !important;
}

div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.9) !important;
    color: #111827 !important;
}
div[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}

.stSelectbox label, .stNumberInput label, .stTextInput label,
.stMultiSelect label {
    color: #94a3b8 !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

.stMultiSelect > div > div {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
}

.stDataFrame { border-radius: 12px; overflow: hidden; }

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* Divider */
hr { border-color: rgba(255,255,255,0.1) !important; margin: 1.5rem 0 !important; }

/* Info / warning boxes */
.stAlert { border-radius: 12px !important; }

.stat-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.stat-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 14px;
    padding: 1.2rem;
    text-align: center;
}

.stat-value { font-size: 1.9rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; }
.stat-label { color: #64748b; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 0.2rem; }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# SESSION STATE INIT
# ──────────────────────────────────────────────
def init_state():
    defaults = {
        "page": "home",          # home | quiz | results | leaderboard
        "questions": [],
        "current_idx": 0,
        "score": 0,
        "answers": [],           # list of dicts: {question, chosen, correct, is_correct}
        "answered": False,
        "chosen": None,
        "player_name": "",
        "score_saved": False,
        "quiz_config": {},
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ──────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────
ALL_CATEGORIES = sorted(set(q["category"] for q in QUESTIONS))
ALL_DIFFICULTIES = ["Easy", "Medium", "Hard"]

DIFF_BADGE = {"Easy": "badge-easy", "Medium": "badge-med", "Hard": "badge-hard"}
EMOJIS = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

def difficulty_badge(d):
    return f'<span class="badge {DIFF_BADGE.get(d, "badge-easy")}">{EMOJIS.get(d,"")} {d}</span>'

def category_badge(c):
    return f'<span class="badge badge-cat">📂 {c}</span>'

def get_grade(pct):
    if pct >= 90: return "🏆 Outstanding!", "#4ade80"
    if pct >= 75: return "🌟 Great Job!", "#818cf8"
    if pct >= 60: return "👍 Good Effort!", "#fbbf24"
    if pct >= 40: return "📚 Keep Studying!", "#fb923c"
    return "💪 Never Give Up!", "#f87171"


def filter_questions(categories, difficulties):
    filtered = QUESTIONS
    if categories:
        filtered = [q for q in filtered if q["category"] in categories]
    if difficulties:
        filtered = [q for q in filtered if q["difficulty"] in difficulties]
    return filtered


def start_quiz(n, categories, difficulties, player_name):
    pool = filter_questions(categories, difficulties)
    if not pool:
        st.error("No questions match your filters. Please adjust your selection.")
        return False
    n = min(n, len(pool))
    selected = random.sample(pool, n)
    # Shuffle options for each question
    shuffled = []
    for q in selected:
        q2 = q.copy()
        opts = q2["options"].copy()
        random.shuffle(opts)
        q2["options"] = opts
        shuffled.append(q2)

    st.session_state.questions = shuffled
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.answered = False
    st.session_state.chosen = None
    st.session_state.player_name = player_name.strip() or "Anonymous"
    st.session_state.score_saved = False
    st.session_state.quiz_config = {
        "categories": categories or ALL_CATEGORIES,
        "difficulties": difficulties or ALL_DIFFICULTIES,
        "n": n,
    }
    st.session_state.page = "quiz"
    return True


# ──────────────────────────────────────────────
# PAGE: HOME
# ──────────────────────────────────────────────
def page_home():
    st.markdown("""
    <div class="hero-card">
        <div class="hero-title">🧠 DS & AI Quiz</div>
        <div class="hero-subtitle">Test your knowledge in Machine Learning, Deep Learning,<br>NLP, Statistics, MLOps and more.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("#### 👤 Your Name")
        player_name = st.text_input("player_name_input", placeholder="Enter your name...", label_visibility="collapsed")

    with col2:
        st.markdown("#### ❓ Questions")
        available_max = len(QUESTIONS)
        n_questions = st.number_input(
            "n_q", min_value=5, max_value=available_max, value=10,
            step=5, label_visibility="collapsed"
        )

    st.markdown("#### 📂 Categories")
    categories = st.multiselect(
        "cats",
        options=ALL_CATEGORIES,
        default=[],
        placeholder="All categories (leave empty for all)",
        label_visibility="collapsed"
    )

    st.markdown("#### 🎯 Difficulty")
    difficulties = st.multiselect(
        "diffs",
        options=ALL_DIFFICULTIES,
        default=[],
        placeholder="All difficulties (leave empty for all)",
        label_visibility="collapsed"
    )

    # Preview count
    pool = filter_questions(categories, difficulties)
    actual_n = min(n_questions, len(pool))
    if pool:
        st.markdown(
            f'<div style="color:#64748b; font-size:0.88rem; margin: 0.5rem 0 1rem;">🎲 {len(pool)} questions available → you\'ll get <b style="color:#818cf8">{actual_n}</b> randomly selected</div>',
            unsafe_allow_html=True
        )
    else:
        st.warning("No questions match the current filters.")

    st.markdown("<br>", unsafe_allow_html=True)
    col_start, col_lb = st.columns([2, 1])
    with col_start:
        if st.button("🚀 Start Quiz", use_container_width=True):
            start_quiz(n_questions, categories, difficulties, player_name)
            st.rerun()
    with col_lb:
        if st.button("🏆 Leaderboard", use_container_width=True):
            st.session_state.page = "leaderboard"
            st.rerun()

    # Stats footer
    st.markdown("<hr>", unsafe_allow_html=True)
    cat_counts = {}
    for q in QUESTIONS:
        cat_counts[q["category"]] = cat_counts.get(q["category"], 0) + 1

    st.markdown(f"""
    <div class="stat-grid">
        <div class="stat-box">
            <div class="stat-value" style="color:#818cf8">{len(QUESTIONS)}</div>
            <div class="stat-label">Total Questions</div>
        </div>
        <div class="stat-box">
            <div class="stat-value" style="color:#c084fc">{len(ALL_CATEGORIES)}</div>
            <div class="stat-label">Categories</div>
        </div>
        <div class="stat-box">
            <div class="stat-value" style="color:#38bdf8">3</div>
            <div class="stat-label">Difficulty Levels</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────
# PAGE: QUIZ
# ──────────────────────────────────────────────
def page_quiz():
    qs = st.session_state.questions
    idx = st.session_state.current_idx
    total = len(qs)

    if idx >= total:
        st.session_state.page = "results"
        st.rerun()
        return

    q = qs[idx]
    pct_done = idx / total

    # ── Progress bar
    st.markdown(f"""
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.3rem;">
        <span style="color:#64748b; font-size:0.82rem; font-family:'JetBrains Mono',monospace;">
            Question {idx+1} of {total}
        </span>
        <span style="color:#818cf8; font-size:0.82rem; font-family:'JetBrains Mono',monospace;">
            Score: {st.session_state.score}/{idx}
        </span>
    </div>
    <div class="progress-container">
        <div class="progress-fill" style="width:{int(pct_done*100)}%"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Question card
    diff = q["difficulty"]
    cat = q["category"]
    st.markdown(f"""
    <div class="question-card">
        <div class="question-meta">
            {category_badge(cat)}
            {difficulty_badge(diff)}
        </div>
        <p class="question-text">{q['question']}</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Answer options
    if not st.session_state.answered:
        chosen = st.radio(
            "Choose your answer:",
            q["options"],
            key=f"radio_{idx}",
            label_visibility="collapsed",
        )
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✅ Submit Answer", use_container_width=True):
            st.session_state.answered = True
            st.session_state.chosen = chosen
            is_correct = chosen == q["answer"]
            if is_correct:
                st.session_state.score += 1
            st.session_state.answers.append({
                "question": q["question"],
                "category": q["category"],
                "difficulty": q["difficulty"],
                "chosen": chosen,
                "correct": q["answer"],
                "is_correct": is_correct,
                "explanation": q.get("explanation", ""),
            })
            st.rerun()
    else:
        chosen = st.session_state.chosen
        is_correct = chosen == q["answer"]

        # Show options greyed out
        st.radio(
            "Your answer:",
            q["options"],
            index=q["options"].index(chosen),
            key=f"radio_done_{idx}",
            disabled=True,
            label_visibility="collapsed",
        )

        if is_correct:
            st.markdown(f'<div class="feedback-correct">✅ Correct! Well done.</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="feedback-wrong">❌ Incorrect. The correct answer is: <b>{q["answer"]}</b></div>',
                unsafe_allow_html=True
            )

        if q.get("explanation"):
            st.markdown(f'<div class="explanation-box">💡 <b>Explanation:</b> {q["explanation"]}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        is_last = (idx + 1 >= total)
        btn_label = "🏁 See Results" if is_last else "➡️ Next Question"
        if st.button(btn_label, use_container_width=True):
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.session_state.chosen = None
            if is_last:
                st.session_state.page = "results"
            st.rerun()

    # Quit button
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏠 Quit to Home", use_container_width=False):
        st.session_state.page = "home"
        st.rerun()


# ──────────────────────────────────────────────
# PAGE: RESULTS
# ──────────────────────────────────────────────
def page_results():
    score = st.session_state.score
    answers = st.session_state.answers
    total = len(answers)
    pct = round(score / total * 100, 1) if total > 0 else 0
    grade, grade_color = get_grade(pct)

    # Save score once
    if not st.session_state.score_saved and answers:
        cfg = st.session_state.quiz_config
        cat_label = ", ".join(cfg.get("categories", ["All"])) if cfg.get("categories") else "All"
        diff_label = ", ".join(cfg.get("difficulties", ["All"])) if cfg.get("difficulties") else "All"
        save_score(
            st.session_state.player_name,
            score, total,
            cat_label[:40],
            diff_label[:30],
        )
        st.session_state.score_saved = True

    # ── Score card
    st.markdown(f"""
    <div class="score-card">
        <div style="font-size:1rem; color:#94a3b8; margin-bottom:0.5rem;">
            {st.session_state.player_name or 'Anonymous'}
        </div>
        <div class="score-number">{score}/{total}</div>
        <div class="score-label">{pct}% correct</div>
        <div style="font-size:1.5rem; margin-top:0.8rem; color:{grade_color};">{grade}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Per-category breakdown
    cat_stats = {}
    for a in answers:
        c = a["category"]
        if c not in cat_stats:
            cat_stats[c] = {"correct": 0, "total": 0}
        cat_stats[c]["total"] += 1
        if a["is_correct"]:
            cat_stats[c]["correct"] += 1

    if len(cat_stats) > 1:
        st.markdown("#### 📊 Breakdown by Category")
        for cat, s in sorted(cat_stats.items()):
            cp = round(s["correct"]/s["total"]*100)
            bar_color = "#4ade80" if cp >= 70 else "#fbbf24" if cp >= 40 else "#f87171"
            st.markdown(f"""
            <div style="margin-bottom:0.7rem;">
                <div style="display:flex; justify-content:space-between; margin-bottom:3px;">
                    <span style="color:#cbd5e1; font-size:0.88rem;">{cat}</span>
                    <span style="color:{bar_color}; font-family:'JetBrains Mono',monospace; font-size:0.88rem;">{s['correct']}/{s['total']}</span>
                </div>
                <div class="progress-container">
                    <div style="height:100%; border-radius:999px; background:{bar_color}; width:{cp}%; transition: width 0.4s;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── Detailed review
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("#### 📝 Answer Review")
    for i, a in enumerate(answers):
        icon = "✅" if a["is_correct"] else "❌"
        color = "#4ade80" if a["is_correct"] else "#f87171"
        with st.expander(f"{icon} Q{i+1}: {a['question'][:70]}..."):
            diff_b = difficulty_badge(a["difficulty"])
            cat_b = category_badge(a["category"])
            st.markdown(f'{cat_b} {diff_b}', unsafe_allow_html=True)
            st.markdown(f"**Your answer:** <span style='color:{color}'>{a['chosen']}</span>", unsafe_allow_html=True)
            if not a["is_correct"]:
                st.markdown(f"**Correct answer:** <span style='color:#4ade80'>{a['correct']}</span>", unsafe_allow_html=True)
            if a.get("explanation"):
                st.markdown(f'<div class="explanation-box">💡 {a["explanation"]}</div>', unsafe_allow_html=True)

    # ── Buttons
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 Play Again", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
    with col2:
        if st.button("🏆 Leaderboard", use_container_width=True):
            st.session_state.page = "leaderboard"
            st.rerun()
    with col3:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()


# ──────────────────────────────────────────────
# PAGE: LEADERBOARD
# ──────────────────────────────────────────────
def page_leaderboard():
    st.markdown('<div class="lb-header">🏆 Leaderboard</div>', unsafe_allow_html=True)
    board = load_leaderboard()

    if not board:
        st.info("No scores yet. Be the first to complete a quiz!")
    else:
        rank_colors = ["#ffd700", "#c0c0c0", "#cd7f32"]
        rank_emojis = ["🥇", "🥈", "🥉"]
        for i, entry in enumerate(board[:20]):
            rank_str = rank_emojis[i] if i < 3 else f"#{i+1}"
            pct_color = "#4ade80" if entry["percentage"] >= 75 else "#fbbf24" if entry["percentage"] >= 50 else "#f87171"
            st.markdown(f"""
            <div class="lb-row">
                <span class="lb-rank">{rank_str}</span>
                <span class="lb-name">{entry['name']}</span>
                <span style="color:#64748b; font-size:0.82rem;">{entry['category'][:25]}</span>
                <span style="color:#64748b; font-size:0.82rem;">{entry['score']}/{entry['total']}</span>
                <span class="lb-pct" style="color:{pct_color}">{entry['percentage']}%</span>
                <span style="color:#475569; font-size:0.75rem;">{entry['date']}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
    with col2:
        if st.button("🗑️ Clear Board", use_container_width=True):
            clear_leaderboard()
            st.rerun()


# ──────────────────────────────────────────────
# ROUTER
# ──────────────────────────────────────────────
page = st.session_state.get("page", "home")

if page == "home":
    page_home()
elif page == "quiz":
    page_quiz()
elif page == "results":
    page_results()
elif page == "leaderboard":
    page_leaderboard()
