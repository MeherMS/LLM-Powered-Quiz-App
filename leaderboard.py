import json
import os
from datetime import datetime

LEADERBOARD_FILE = "leaderboard.json"


def load_leaderboard() -> list[dict]:
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []


def save_score(name: str, score: int, total: int, category: str, difficulty: str):
    board = load_leaderboard()
    entry = {
        "name": name,
        "score": score,
        "total": total,
        "percentage": round(score / total * 100, 1) if total > 0 else 0,
        "category": category,
        "difficulty": difficulty,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    board.append(entry)
    board.sort(key=lambda x: (-x["percentage"], -x["score"]))
    board = board[:50]  # Keep top 50
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(board, f, indent=2)


def clear_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        os.remove(LEADERBOARD_FILE)
