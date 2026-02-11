🤖 Agentic AI Multi-Agent Exam Preparation System

An AI-powered web application that helps students prepare for exams using a multi-agent system.
The system generates study plans, quizzes, evaluates answers, tracks performance, and analyzes weak areas using advanced language models.

Built with Streamlit and powered by Groq Llama AI.

🚀 Features

✅ Personalized study plan generation
✅ Automatic MCQ quiz creation
✅ Answer evaluation with feedback
✅ Score tracking & performance history
✅ Weak topic analysis
✅ Multi-agent architecture
✅ Interactive web interface

🧠 Multi-Agent Architecture

This system uses multiple specialized AI agents:

Agent	Role
Planner Agent	Creates structured study plans
Quiz Agent	Generates MCQs
Evaluator Agent	Checks answers and gives scores
Weakness Analyzer	Identifies weak topics

Each agent works independently and collaborates to provide a complete learning experience.

🛠 Tech Stack

Python

Streamlit

Groq API (Llama-3.3-70B)

Pandas

JSON (for data storage)

Regex & NLP

References

Streamlit: https://docs.streamlit.io

Groq API: https://console.groq.com/docs

Llama Models: https://ai.meta.com/llama

📁 Project Structure
agentic-ai-exam-prep/
│
├── app.py
├── progress_data.json
├── requirements.txt
└── README.md

▶️ How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/your-username/agentic-ai-exam-prep.git
cd agentic-ai-exam-prep

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Up Groq API Key

Create an environment variable:

Windows (PowerShell)
setx GROQ_API_KEY "your_api_key_here"

Linux / Mac
export GROQ_API_KEY="your_api_key_here"


Get API Key from:
https://console.groq.com

4️⃣ Run the Application
streamlit run app.py


Open in browser:

http://localhost:8501

📊 Data Storage

User performance is saved in:

progress_data.json


It stores:

Topic

Score

Date & Time

This enables progress tracking and weak-area analysis.

📈 Application Workflow

Enter topic & duration → Generate study plan

Enter quiz topic → Generate MCQs

Submit answers → Get evaluation

Scores are saved automatically

Analyze weak areas → Get improvement tips

🌐 Deployment

This application can be deployed on:

Streamlit Cloud

Hugging Face Spaces

Any cloud VM (AWS, GCP, Azure)

Streamlit Cloud Guide:

https://docs.streamlit.io/streamlit-community-cloud

Hugging Face Spaces:

https://huggingface.co/docs/hub/spaces

🧪 Example Use Cases

✔ Competitive exam preparation
✔ Self-learning support
✔ Personalized tutoring
✔ Performance monitoring
✔ AI-powered coaching

👩‍💻 Author

Areeba Chaudhry
Software Engineer | AI & ML Enthusiast


📜 License

This project is intended for educational and research purposes.

📚 References

Streamlit Documentation
https://docs.streamlit.io

Groq API Documentation
https://console.groq.com/docs

Llama Models
https://ai.meta.com/llama
