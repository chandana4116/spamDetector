from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        message = request.form["message"]

        # Example spam detection logic (replace with Horspool later)
        if "spam" in message.lower():
            result = "⚠️ Spam detected!"
        else:
            result = "✅ Message looks safe."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
