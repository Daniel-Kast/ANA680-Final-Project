from flask import Flask, render_template, request
import pickle
import numpy as np

# Load model, vectorizer, and class names
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

print("Vectorizer vocabulary size:", len(vectorizer.vocabulary_))

with open("target_names.pkl", "rb") as f:
    target_names = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    top3 = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]

        # Transform text
        X = vectorizer.transform([text])

        # Predict class
        pred = model.predict(X)[0]
        prediction = target_names[pred]

        # Top‑3 scores (SVM decision_function)
        try:
            scores = model.decision_function(X)[0]
            top3_idx = np.argsort(scores)[-3:][::-1]
            top3 = [(target_names[i], float(scores[i])) for i in top3_idx]
        except:
            top3 = None

    return render_template(
        "index.html",
        text=text,
        prediction=prediction,
        top3=top3
    )

if __name__ == "__main__":
    app.run(debug=True)
