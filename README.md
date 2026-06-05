# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python**, **TF-IDF Vectorization**, and **Cosine Similarity**. The application recommends movies similar to a selected movie based on their content and metadata.

## 🚀 Features

* Movie recommendations based on content similarity
* TF-IDF Vectorization for text feature extraction
* Cosine Similarity for finding related movies
* Interactive web interface using Streamlit
* Fast and lightweight recommendation engine
* Clean and responsive UI

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* TF-IDF Vectorizer
* Cosine Similarity

### Dataset

* TMDB 5000 Movie Dataset

---

## 📂 Project Structure

```text
movie-recommendation-system/
│
├── app.py
├── movies.pkl
├── requirements.txt
├── runtime.txt
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── Movies-Recommendation.ipynbw
└── README.md
```

---

## ⚙️ How It Works

### 1. Data Preprocessing

* Load TMDB movie and credits datasets
* Merge datasets
* Extract:

  * Genres
  * Keywords
  * Cast
  * Director
  * Overview

### 2. Feature Engineering

* Combine all relevant information into a single tags column
* Convert text to lowercase
* Apply text cleaning and preprocessing

### 3. TF-IDF Vectorization

Convert movie tags into numerical feature vectors.

### 4. Similarity Calculation

Compute similarity scores using Cosine Similarity.

### 5. Recommendation

When a movie is selected:

* Find its similarity scores
* Sort movies by similarity
* Return the Top 5 recommendations

---

## 📊 Machine Learning Concepts Used

### TF-IDF (Term Frequency - Inverse Document Frequency)

TF-IDF measures the importance of a word in a document relative to the entire dataset.

### Cosine Similarity

Cosine Similarity calculates the similarity between two movie vectors.

The closer the score is to 1, the more similar the movies are.

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/Om-Handa/Movie-Recommendation-System.git
cd movie-recommendation-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

1. Select a movie from the dropdown menu
2. Click **Recommend Movies**
3. View the top recommended movies

---

## 📈 Future Improvements

* Movie posters using TMDB API
* Genre filtering
* Search suggestions
* Hybrid recommendation system
* User authentication
* Movie ratings integration

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Data preprocessing and feature engineering
* Natural Language Processing basics
* TF-IDF Vectorization
* Cosine Similarity
* Content-Based Recommendation Systems
* Streamlit application development
* Model serialization using Pickle

---

## 👨‍💻 Author

**Om Handa**

If you found this project useful, feel free to star the repository ⭐
