# **20 Newsgroups Text Classification — End‑to‑End Machine Learning & Deployment Pipeline**

## Deployment Badges

[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-Image%20Available-blue)](https://hub.docker.com/r/danielkast/newsgroups-app)
[![Heroku](https://img.shields.io/badge/Heroku-Live%20App-purple)](https://ana680-final-dkast-a00995d01ad6.herokuapp.com/)
[![AWS EC2](https://img.shields.io/badge/AWS%20EC2-Live%20Deployment-orange)](http://3.16.76.102)

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Nginx](https://img.shields.io/badge/Nginx-Reverse%20Proxy-green)
![AWS EC2](https://img.shields.io/badge/AWS-EC2-orange)
![Heroku](https://img.shields.io/badge/Heroku-Deployment-purple)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML%20Modeling-orange)

---

# **Project Overview**

This project implements the full machine learning and MLOps pipeline taught in ANA680. The goal is to classify free‑text documents into one of **20 predefined newsgroup categories** using natural language processing (NLP) and supervised machine learning.

The project includes:

- Data exploration and preprocessing  
- Model training and evaluation  
- Local Flask deployment  
- Docker containerization  
- CI/CD deployment to Heroku  
- Full production deployment on **AWS EC2 using Docker + Nginx**  

All artifacts are included in this repository for instructor review.

---

# **1. Problem Definition**

Organizations generate large volumes of unstructured text (emails, articles, reports). Manually categorizing these documents is slow, inconsistent, and not scalable.

Machine learning provides the best solution because it:

- Learns patterns from labeled text  
- Generalizes to unseen documents  
- Produces consistent, repeatable classifications  
- Scales instantly  

### **Dataset**

The project uses the **20 Newsgroups dataset**, accessed via:

```
sklearn.datasets.fetch_20newsgroups
```

It contains ~18,000 documents across 20 categories, including politics, sports, religion, science, and technology.

A full category list is included later in this README.

---

# **2. Data Exploration, Cleaning, and Feature Engineering**

All exploration and preprocessing steps were completed in `notebooks/project.ipynb`.

### **Exploration**
- Class distribution  
- Word counts  
- Example documents  
- Vocabulary inspection  

### **Cleaning**
- Lowercasing  
- Stopword removal  
- Tokenization  

### **Feature Engineering**
- TF‑IDF vectorization  
- `max_features = 20,000`  
- Sparse matrix representation  

All training code is included in the repository.

---

# **3. Model Training, Evaluation, and Saved Artifacts**

### **Train/Test/Validation Split**
- 80% training  
- 20% testing  
- Validation via cross‑validation  

### **Model**
- **Linear Support Vector Classifier (LinearSVC)**  
- Chosen for:
  - High performance on sparse text  
  - Fast training  
  - Strong generalization  

### **Evaluation Metrics**
- Accuracy  
- Decision function scores  
- Top‑3 predicted categories  

### **Saved Artifacts**
All saved in the repo:

- `model.pkl` — trained SVM model  
- `vectorizer.pkl` — TF‑IDF vectorizer  
- `target_names.pkl` — category labels  

---

# **4. Local Flask Deployment**

A simple web interface was built using Flask to allow users to paste text and receive predictions.

### **Run Locally**

```bash
pip install -r requirements.txt
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

A screenshot of the local deployment is included in `assets/`.

---

# **5. Docker Containerization**

The Flask app was containerized using a `Dockerfile`.

### **Build and Run**

```bash
docker build -t newsgroups-app .
docker run -p 5000:5000 newsgroups-app
```

The app becomes available at:

```
http://localhost:5000
```

The image was pushed to Docker Hub:

```
danielkast/newsgroups-app:latest
```

---

# **6. CI/CD Pipeline + Heroku Deployment**

A CI/CD pipeline was created using GitHub → Heroku integration.

### **Required Files**
- `Procfile`  
- `requirements.txt`  
- `runtime.txt`  
- `Dockerfile` (optional for container deploy)  
- `app.py`  
- `templates/index.html`  

Heroku automatically built and deployed the application on push to `main`.

Live app:  
[https://ana680-final-dkast-a00995d01ad6.herokuapp.com/](https://ana680-final-dkast-a00995d01ad6.herokuapp.com/)

---

# **7. AWS EC2 Deployment Using Docker + Nginx**

The project was redeployed on **AWS EC2** using:

- Amazon Linux 2023  
- Docker Engine  
- Docker Hub image  
- Custom Docker network  
- Nginx reverse proxy  

### **Steps Completed**

#### **1. Launch EC2 Instance**
- Amazon Linux 2023  
- t2.micro  
- Security group:
  - SSH (22) — My IP  
  - HTTP (80) — Anywhere  

#### **2. Install Docker**
```
sudo yum update -y
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
```

#### **3. Pull Project Image**
```
docker pull danielkast/newsgroups-app:latest
```

#### **4. Create Docker Network**
```
docker network create projectnet
```

#### **5. Run App Container**
```
docker run -d --name project --network projectnet danielkast/newsgroups-app:latest
```

#### **6. Create nginx.conf**
```
events {}

http {
    server {
        listen 80;

        location / {
            proxy_pass http://project:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```

#### **7. Run Nginx Container**
```
docker run -d --name nginx --network projectnet -p 80:80 \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro nginx:alpine
```

#### **8. Access the Live App**
```
http://3.16.76.102
```

A screenshot of the live EC2 deployment is included in `assets/`.

---

# **8. Deployment Documentation (This README)**

This README provides a complete walkthrough of:

- ML problem definition  
- Data exploration and modeling  
- Local Flask deployment  
- Docker containerization  
- CI/CD pipeline  
- Heroku deployment  
- AWS EC2 + Nginx deployment  

Anyone following this document can reproduce the entire project end‑to‑end.

---

# **Dataset Categories**

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

# **File Structure**

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
│   ├── localhost_screenshot.png
│   └── ec2_screenshot.png
├── templates/
│   └── index.html
└── notebooks/
    └── project.ipynb
```

---

# **Author**

**Daniel Kast**  
ANA680 Final Project  
National University  


