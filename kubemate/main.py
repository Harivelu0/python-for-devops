from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from dotenv import load_dotenv
import os
import markdown

from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain

#  Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(" GEMINI_API_KEY not set in .env")

#  Initialize Gemini with LangChain
llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", google_api_key=api_key)

#  Memory for chat history
memory = ConversationBufferMemory()

#  LangChain ConversationChain setup
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

#  Initialize Flask
app = Flask(__name__)
app.secret_key = "super-secret-kubemate"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    user_input = ""

    if "chat_history" not in session:
        session["chat_history"] = []

    try:
        if request.method == "POST":
            uploaded_file = request.files.get("file")
            user_input = request.form.get("log_input", "")
            file_content = uploaded_file.read().decode("utf-8") if uploaded_file and uploaded_file.filename else ""
            final_input = file_content or user_input

            if final_input.strip():
                prompt = "You're a Kubernetes DevOps expert. Analyze this:\n\n"
                prompt += final_input.strip()
                prompt += "\n\nExplain the issue and suggest how to fix it."

                # Call Gemini via LangChain
                result = conversation.run(prompt)

                # Convert to Markdown for UI rendering
                response_text = markdown.markdown(result)

                # Store in session history
                session["chat_history"].append({
                    "input": final_input.strip(),
                    "output": response_text.strip()
                })
                session.modified = True

    except Exception as e:
        response_text = f"<span style='color:red'> Gemini Error: {e}</span>"

    user_input = ""  # Clear input so textarea is empty after submit
    return render_template("index.html", response=response_text, user_input=user_input, chat_history=session["chat_history"])


#  Clear chat history route
@app.route("/clear")
def clear_history():
    session["chat_history"] = []
    memory.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
