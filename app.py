import os
import json
import re
from datetime import datetime

import streamlit as st
import pandas as pd
from groq import Groq


# ==============================
# CONFIG
# ==============================

st.set_page_config(page_title="Agentic AI Exam Preparation", layout="wide")

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

DATA_FILE = "progress_data.json"


# ==============================
# DATA FUNCTIONS
# ==============================

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def extract_score(text):
    match = re.search(r"(\d+(\.\d+)?)/10", text)
    if match:
        return float(match.group(1))
    return None


def call_agent(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content


# ==============================
# AGENT PROMPTS
# ==============================

PLANNER_PROMPT = """
You are a Planner Agent in an Agentic AI system.
Create a structured study plan based on:
- Topic
- Duration (1 Week, 2 Week, 3 Week, 1 Month, 2 Months, 3 Months, 4 Months, 5 Months, 6 Months)
Rules:
- 1 Week → Daily breakdown
- 1 Month → Weekly breakdown
- 3 Months+ → Monthly focus + weekly milestones
- Include objectives, time allocation, resources, and practice strategy
"""

QUIZ_PROMPT = """
You are a Quiz Agent.
Generate 5 multiple-choice questions (MCQs).
Rules:
- Provide only questions
- Each question must have 4 options (A, B, C, D)
- Do NOT provide answers
- Clear formatting
"""

EVALUATOR_PROMPT = """
You are an Evaluator Agent.
Evaluate the student's answers.
Provide:
1. Correct answers
2. Score out of 10 (e.g., 8/10 or 8.5/10)
3. Brief explanation for wrong answers
"""

WEAKNESS_PROMPT = """
You are a Weak Topic Analyzer Agent.
Analyze performance history.
Identify weak topics and suggest improvement strategies.
"""


# ==============================
# APP TITLE
# ==============================

st.title("🤖 Agentic AI Multi-Agent Exam Preparation System")

data = load_data()


# ==============================
# 📅 PLANNER AGENT
# ==============================

st.header("📅 Planner Agent")

planner_topic = st.text_input("Enter Topic for Study Plan")

duration = st.selectbox(
    "Select Study Duration",
    [
        "1 Week", "2 Week", "3 Week",
        "1 Month", "2 Months", "3 Months",
        "4 Months", "5 Months", "6 Months"
    ]
)

if st.button("Generate Study Plan"):
    if planner_topic:
        prompt = f"Topic: {planner_topic}\nDuration: {duration}"
        plan = call_agent(PLANNER_PROMPT, prompt)
        st.success("Study Plan Generated")
        st.write(plan)
    else:
        st.warning("Please enter a topic for study plan.")


# ==============================
# 📝 QUIZ AGENT
# ==============================

st.header("📝 Quiz Agent (MCQ Mode)")

quiz_topic = st.text_input("Enter Topic for Quiz")

if st.button("Generate MCQ Quiz"):
    if quiz_topic:
        quiz = call_agent(QUIZ_PROMPT, quiz_topic)

        st.session_state["quiz"] = quiz
        st.session_state["quiz_topic"] = quiz_topic

        st.success("Quiz Generated")
        st.write(quiz)

    else:
        st.warning("Please enter a quiz topic.")


# ==============================
# 📊 MCQ EVALUATION
# ==============================

st.header("📊 Submit Your Answers")

user_mcq_answers = st.text_area(
    "Enter answers like: 1-A, 2-C, 3-B, 4-D, 5-A"
)

if st.button("Evaluate MCQs"):

    if "quiz" in st.session_state and user_mcq_answers:

        evaluation_prompt = f"""
Topic: {st.session_state.get("quiz_topic", "General")}
Quiz:
{st.session_state["quiz"]}
Student Answers:
{user_mcq_answers}
"""

        evaluation = call_agent(EVALUATOR_PROMPT, evaluation_prompt)

        st.subheader("Evaluation Result")
        st.write(evaluation)

        score = extract_score(evaluation)

        if score is not None:

            new_entry = {
                "topic": st.session_state.get("quiz_topic", "General"),
                "score": float(score),
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            data.append(new_entry)
            save_data(data)

            st.success(f"Score saved: {score}/10")

    else:
        st.warning("Generate a quiz and enter answers first.")


# ==============================
# 📈 PERFORMANCE HISTORY
# ==============================

st.header("📈 Performance History")

if data:

    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    st.dataframe(df)

else:
    st.info("No performance data yet.")


# ==============================
# 🔍 WEAK TOPIC ANALYZER
# ==============================

st.header("🔍 Weak Topic Analyzer Agent")

if st.button("Analyze Weak Areas"):

    if data:

        history_text = "\n".join(
            [f"{d['topic']} - {d['score']}/10" for d in data]
        )

        analysis = call_agent(WEAKNESS_PROMPT, history_text)

        st.subheader("Analysis Result")
        st.write(analysis)

    else:
        st.info("Not enough data for analysis.")
