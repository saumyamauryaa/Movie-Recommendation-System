import pickle, os, pandas as pd, numpy as np

# Make sure model folder exists
os.makedirs('model', exist_ok=True)

# Create some example movies
movies = pd.DataFrame({
    'movie_id': [27205, 157336, 19995, 155, 597],
    'title': ['Inception', 'Interstellar', 'Avatar', 'The Dark Knight', 'Titanic']
})

# Create a simple similarity matrix (so the app runs)
similarity = np.eye(len(movies))

# Save the files
pickle.dump(movies, open('model/movie_list.pkl', 'wb'))
pickle.dump(similarity, open('model/similarity.pkl', 'wb'))

print("✅ Created movie_list.pkl and similarity.pkl successfully!")
