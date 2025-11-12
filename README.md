🎬 Movie Recommender System

A content-based movie recommender system built with Python, Streamlit, and TMDB API.
This app recommends movies similar to the one you select and displays their posters, fetched dynamically from the TMDB database.

🚀 Features

✅ Select a movie from the dropdown
✅ Get 5 most similar movie recommendations
✅ Display movie posters from TMDB
✅ Simple, interactive Streamlit interface
✅ Easily expandable with real datasets or ML models

🧠 How It Works

This app uses a content-based filtering approach:

Loads preprocessed movie data (movie_list.pkl)

Uses a similarity matrix (similarity.pkl) to find the most similar titles

Fetches posters and details via TMDB API

Displays results in a clean, visual layout

🗂️ Project Structure
movie_recommendor/
│
├── app.py                    # Main Streamlit app
├── create_model_files.py     # Script to create dummy model files
├── model/
│   ├── movie_list.pkl        # Pickled movie data (pandas DataFrame)
│   └── similarity.pkl        # Pickled similarity matrix
│
└── README.md                 # Project documentation

🧩 Setup Instructions

Follow these steps to run the project locally 👇

1️⃣ Clone this repository
git clone https://github.com/<your-username>/movie-recommendor.git
cd movie-recommendor

2️⃣ Install dependencies

Make sure Python is installed (Python 3.8+ recommended).

pip install streamlit requests pandas

3️⃣ (Optional) Create dummy model files

If you don’t have the real model files yet, you can generate small placeholder ones to test your app.

Run this once:

python create_model_files.py


You should see:

✅ Model files created successfully in 'model/' folder

4️⃣ Run the app

Start your Streamlit app:

streamlit run app.py


Then open the provided local URL (usually http://localhost:8505
).

🧠 Example Output

When running successfully, you’ll see:

A dropdown to select any movie

“Show Recommendation” button

Posters + titles of top 5 similar movies

🔑 API Information

This app uses the TMDB API to fetch poster images.
API URL:

https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8


If you’d like to use your own TMDB API key, sign up at
👉 https://www.themoviedb.org/

Then replace the API key inside app.py:

url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"

⚙️ Future Improvements

💡 Use real datasets from Kaggle (like TMDB 5000 Movie Dataset)
💡 Implement cosine similarity for better accuracy
💡 Add movie overview and rating display
💡 Deploy online (Streamlit Cloud / Render / Hugging Face Spaces)

🤝 Contributing

Contributions are welcome!

Fork this repo

Create a new branch (feature/my-improvement)

Commit and push your changes

Open a pull request

🪪 License

This project is licensed under the MIT License — feel free to use and modify it for personal or educational purposes.

💬 Example Run Command (Quick Start)
pip install streamlit requests pandas
python create_model_files.py
streamlit run app.py
