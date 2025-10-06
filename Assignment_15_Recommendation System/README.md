# 🎌 Anime Recommendation System 🎌

## 🚀 Project Overview
This project builds a content-based recommendation system for anime using the "anime.csv" dataset. The system recommends similar anime based on genres, ratings, and popularity, using cosine similarity to find close matches. 🎥⭐

## 📊 Dataset
The `anime.csv` dataset contains:
- `anime_id`: Unique identifier for each anime
- `name`: Anime title
- `genre`: Genres associated with the anime (multiple possible)
- `type`: Type of anime (TV, Movie, OVA, etc.)
- `episodes`: Number of episodes
- `rating`: Average user rating 🎖️
- `members`: Number of members in the community 👥

## 🧹 Data Preprocessing
- Cleaned data by removing missing values in key columns.
- Converted genre strings into lists and applied one-hot encoding with `MultiLabelBinarizer`. 🎭
- Normalized numerical features (`rating`, `members`) using `MinMaxScaler`. 📏
- Combined all features into a matrix for similarity calculations.

## 🤖 Recommendation Methodology
- Computed cosine similarity between anime feature vectors.
- Created a recommendation function that takes an anime title and returns a list of similar anime based on similarity scores. 🧩
- Parameters allow control over number of recommendations and similarity threshold.

## 🎯 How to Use
1. Load and preprocess the anime dataset.
2. Call the recommendation function with an anime title to get similar anime suggestions.
3. Adjust parameters to get more precise or broader recommendations.

## 🌟 Future Improvements
- Add collaborative filtering using user interaction data for personalized recommendations. 👤
- Include more metadata features for enhanced recommendations.
- Explore hybrid models combining content-based and collaborative approaches.

## ❓ Interview Topics Covered
- Difference between user-based and item-based collaborative filtering.
- Explanation of collaborative filtering techniques.

---

Enjoy exploring new anime tailored to your taste! 🍿✨
