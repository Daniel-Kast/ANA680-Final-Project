# 20 Newsgroups Text Classification

## Project Overview

This project implements an end-to-end machine learning pipeline to classify free-text documents into one of **20 predefined newsgroup categories**. It uses **TF-IDF vectorization** and a **Linear Support Vector Machine (SVM)** to predict the most relevant topic based on user input.

The trained model is deployed through a **Flask web application** and fully **containerized with Docker**, making it portable and easy to run across environments.

---

## Problem Statement

Manually categorizing large volumes of text documents is time-consuming, inconsistent, and error-prone. Machine learning provides a scalable solution by learning patterns from labeled data and generalizing those patterns to unseen documents.

This project demonstrates how **natural language processing (NLP)** and **supervised machine learning** can be used to automate document classification efficiently and accurately.

---

## Dataset

The project uses the **20 Newsgroups** dataset, available through `sklearn.datasets.fetch_20newsgroups`. The dataset contains approximately **18,000 documents** across 20 topical categories:

1. alt.atheism
2. comp.graphics
3. comp.os.ms-windows.misc
4. comp.sys.ibm.pc.hardware
5. comp.sys.mac.hardware
6. comp.windows.x
7. misc.forsale
8. rec.autos
9. rec.motorcycles
10. rec.sport.baseball
11. rec.sport.hockey
12. sci.crypt
13. sci.electronics
14. sci.med
15. sci.space
16. soc.religion.christian
17. talk.politics.guns
18. talk.politics.mideast
19. talk.politics.misc
20. talk.religion.misc

---

## Model Pipeline

**Preprocessing**

* Text cleaning and stopword removal
* TF-IDF vectorization with `max_features = 20000`

**Model**

* Linear Support Vector Classifier (LinearSVC)

**Evaluation**

* Classification accuracy
* Top-3 category decision scores

**Saved Artifacts**

* `model.pkl` — trained SVM classifier
* `vectorizer.pkl` — TF-IDF vectorizer
* `target_names.pkl` — category labels

---

## Local Deployment

To run the application locally:

```bash
# Navigate to the project directory
cd ANA680-Final-Project

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

Enter text into the form and click **Predict Category** to view the predicted newsgroup.

---

## Docker Deployment

Build and run the Docker container:

```bash
# Build the Docker image
docker build -t newsgroups-app .

# Run the container
docker run -p 5000:5000 newsgroups-app
```

The application will be accessible at:

```
http://localhost:5000
```

---

## Heroku Deployment

Ensure the repository includes the following files:

* `Procfile`
* `requirements.txt`
* `runtime.txt`
* `app.py`
* `templates/index.html`

Deploy using **Heroku GitHub integration** or a **CI/CD workflow**.

---

## AWS EC2 + Nginx Deployment

High-level deployment steps:

1. Launch an Ubuntu EC2 instance
2. Install Docker
3. Pull the Docker image from Docker Hub
4. Run the container on port 5000
5. Install and configure **nginx** as a reverse proxy to the Flask container

---

## Screenshot

A screenshot of the running application is included in the `assets/` directory.

---

## File Structure

```text
ANA680-Final-Project/
├── app.py
├── model.pkl
├── vectorizer.pkl
├── target_names.pkl
├── requirements.txt
├── Dockerfile
├── Procfile
├── runtime.txt
├── README.md
├── assets/
│   └── localhost_screenshot.png
├── templates/
│   └── index.html
└── notebooks/
    └── project.ipynb
```

---

## Author

**Daniel Kast**
ANA680 Final Project
National University

---

## License

MIT License (optional)
