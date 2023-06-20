import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD

# Function to perform text clustering
def cluster_text(data):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data)
    
    # Reduce dimensionality
    svd = TruncatedSVD(n_components=2)
    X = svd.fit_transform(X)
    
    # Perform clustering
    kmeans = KMeans(n_clusters=4, random_state=0)
    kmeans.fit(X)
    
    return kmeans.labels_

# Function to suggest new categories
def suggest_categories(data):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(data)
    
    # Reduce dimensionality
    svd = TruncatedSVD(n_components=2)
    X = svd.fit_transform(X)
    
    # Perform clustering
    kmeans = KMeans(n_clusters=4, random_state=0)
    kmeans.fit(X)
    
    # Get cluster centers
    cluster_centers = kmeans.cluster_centers_
    
    # Perform similarity search
    similarities = []
    for i in range(len(data)):
        text_vector = X[i]
        similarity = []
        for center in cluster_centers:
            similarity.append(cosine_similarity(text_vector.reshape(1, -1), center.reshape(1, -1)))
        max_similarity = max(similarity)
        similarities.append(max_similarity)
    
    # Sort the texts by similarity and suggest categories for top 3
    sorted_indices = sorted(range(len(similarities)), key=lambda k: similarities[k], reverse=True)
    top_texts = [data[i] for i in sorted_indices[:3]]
    
    return top_texts

# Main function to run the app
def main():
    st.title("Support Request Categorization")
    
    # Read CSV file
    file = st.file_uploader("Upload CSV file", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        support_requests = df['Request'].tolist()
        
        # Perform clustering
        labels = cluster_text(support_requests)
        
        # Categorized requests
        categories = ['Software', 'Hardware', 'General Media', 'Other']
        categorized_requests = {category: [] for category in categories}
        for i, label in enumerate(labels):
            categorized_requests[categories[label]].append(support_requests[i])
        
        # Display categorized requests
        st.subheader("Categorized Requests")
        for category, requests in categorized_requests.items():
            st.write(f"**{category}**: {len(requests)} requests")
            for request in requests:
                st.write(request)
        
        # Suggest new categories
        suggested_categories = suggest_categories(support_requests)
        
        # Display suggested categories
        st.subheader("Suggested Categories")
        for i, category in enumerate(suggested_categories):
            st.write(f"**Suggested Category {i+1}**: {category}")
    
if __name__ == "__main__":
    main()
