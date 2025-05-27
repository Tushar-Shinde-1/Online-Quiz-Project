# 🎓 Online Quiz Application

This is a **command-line based quiz application** developed in **Python** that allows users to take quizzes on subjects like Python, FDS, and C Language. It offers different levels of difficulty and provides interactive feedback based on performance.

---

## ✨ Features

- 👨‍🎓 User-friendly welcome interface
- 📚 Subject selection: Python 🐍, FDS 💾, C Language 🖥️
- 🧠 Difficulty Levels: Easy 🟢, Medium 🟡, Hard 🔴
- ⏳ 10-minute timer to complete the quiz
- ✅ 10 randomized multiple-choice questions
- 📊 Real-time performance stats
- 📝 View correct answers (Answer key)
- 🔁 Option to retake the quiz

---

## 📁 Dataset

- Quiz questions are read from an **Excel file** (`datasetpython.xlsx`)
- The Excel file should contain **separate sheets** for:
  - `PYTHON-EASY`, `PYTHON-MEDIUM`, `PYTHON-HARD`
  - `FDS-EASY`, `FDS-MEDIUM`, `FDS-HARD`
  - `C-EASY`, `C-MEDIUM`, `C-HARD`

Each sheet must have the following columns:
- `Sr.No.`
- `Question`
- `A`, `B`, `C`, `D` (Options)
- `Answer` (Correct option: A/B/C/D)

---

## 🛠 Requirements

- Python 3.x
- `pandas`
- `openpyxl`

Install dependencies using:

```bash
pip install pandas openpyxl
```
▶️ How to Run
Make sure the Excel file (datasetpython.xlsx) is present in the same directory.

Run the Python file:
```


