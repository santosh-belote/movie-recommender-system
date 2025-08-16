# movie-recommender-system-tmdb-dataset
A content based movie recommender system using cosine similarity

**Steps:**

1. Combine movies and credits dataset and create a single pandas dataframe.
2. Check and Remove Duplicate (if any)
3. Check and Handle null values (if any)
4. Perform Feature Engineering and drop unwanted features
5. Create tags for movies by combining different features
6. Convert list of tags into String
7. Convert All the tags into lower case (Recommended)
8. Perform Stemming on tags to bring different forms of words to its root version
9. Perform Vectorizarion and Create vectors of these tags. (Represent each movie with a vector in multidimentional space)
10. Find Similarity matrix (cosin similarity) of the movies
11. Based on similarity matrix recommend 5 similar movies
