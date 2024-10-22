import requests
import pandas as pd
import streamlit as st
import re

def clean_text(text):
    if pd.isna(text):
        return ""
    
    # Convert to string if not already
    text = str(text)
    
    # Remove common list markers (numbers, letters, bullets)
    text = re.sub(r'^\s*[\(\[\{]?[0-9a-zA-Z][\)\]\}]?\s*[\.,-]\s*', '', text)
    text = re.sub(r'^\s*[\-\*\•\◦\○\⚬]+\s*', '', text)
    
    # Remove any remaining parentheses, brackets, and their contents
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[[^\]]*\]', '', text)
    text = re.sub(r'\{[^}]*\}', '', text)
    
    # Remove special characters but keep hyphens within words
    text = re.sub(r'[^a-zA-Z0-9\s\-]', ' ', text)
    
    # Replace multiple hyphens with single hyphen
    text = re.sub(r'-+', '-', text)
    
    # Remove hyphens at start or end
    text = re.sub(r'^-+|-+$', '', text)
    
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    
    # Strip whitespace
    text = text.strip()
    
    return text

def clean_dataframe(df):
    # Make a copy to avoid modifying the original
    df_cleaned = df.copy()
    
    # Clean the 'term' column
    if 'term' in df_cleaned.columns:
        df_cleaned['term'] = df_cleaned['term'].apply(clean_text)
        
        # Remove empty rows
        df_cleaned = df_cleaned[df_cleaned['term'].str.len() > 0]
        
        # Remove duplicates
        df_cleaned = df_cleaned.drop_duplicates(subset=['term'])
    
    return df_cleaned

def search_wikidata(query, limit=5):
    url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbsearchentities",
        "format": "json",
        "language": "en",
        "type": "item",
        "limit": limit,
        "search": query
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    results = []
    for result in data.get("search", []):
        results.append({
            "id": result["id"],
            "label": result.get("label", "No label"),
            "description": result.get("description", "No description available")
        })
    return results

def main():
    st.title("Legal Concepts Wikidata Mapper")

    st.markdown("""
    ## Welcome to the Legal Concepts Wikidata Mapper!

    This app helps you map legal terms and concepts to their corresponding Wikidata entities. 
    It includes automatic data cleaning to handle messy input data!

    ### Data Cleaning Features:
    - Removes list markers (numbers, bullets, etc.)
    - Strips unnecessary punctuation and special characters
    - Removes empty rows and duplicates
    - Cleans up extra spaces and formatting
    - Preserves hyphens within words
    
    ### How it works:
    1. **Upload a CSV file**: Your file should contain a column named 'term' with the legal terms you want to map.
    2. **Data Cleaning**: The app automatically cleans your data.
    3. **Review Changes**: You can see both original and cleaned data.
    4. **Search Wikidata**: For each cleaned term, the app searches Wikidata.
    5. **Select matches**: Choose the most appropriate Wikidata entity for each term.
    6. **Download results**: Get a new CSV file with the Wikidata IDs added.
    """)

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        # Read original data
        df_original = pd.read_csv(uploaded_file)
        
        if 'term' not in df_original.columns:
            st.error("The CSV file must contain a 'term' column. Please check your file and try again.")
            return

        # Clean the data
        df_cleaned = clean_dataframe(df_original)
        
        # Show data cleaning results
        st.markdown("### Data Cleaning Results")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Original Data:")
            st.write(df_original[['term']].head())
        
        with col2:
            st.write("Cleaned Data:")
            st.write(df_cleaned[['term']].head())
            
        st.write(f"Rows before cleaning: {len(df_original)}")
        st.write(f"Rows after cleaning: {len(df_cleaned)}")
        
        if len(df_original) != len(df_cleaned):
            st.info(f"Removed {len(df_original) - len(df_cleaned)} duplicate or empty rows during cleaning.")

        proceed = st.button("Proceed with Cleaned Data")
        
        if proceed:
            st.markdown("### Mapping Process")
            st.write("For each cleaned term, we'll search Wikidata and ask you to select the best match.")

            results = {}
            for term in df_cleaned['term']:
                with st.expander(f"Map '{term}'"):
                    st.write(f"Searching Wikidata for '{term}'...")
                    wikidata_results = search_wikidata(term)
                    if wikidata_results:
                        options = [f"{r['id']} - {r['label']} ({r['description']})" for r in wikidata_results]
                        selected = st.selectbox(
                            f"Select the appropriate Wikidata entity for '{term}':", 
                            options + ['None of the above']
                        )
                        if selected != 'None of the above':
                            results[term] = selected.split(' - ')[0]
                            st.success(f"Mapped '{term}' to Wikidata entity {results[term]}")
                        else:
                            results[term] = ''
                            st.info("Term will be left unmapped")
                    else:
                        st.write("No results found. Term will be left unmapped.")
                        results[term] = ''

            df_cleaned['wikidata_id'] = df_cleaned['term'].map(results)

            st.markdown("### Final Results")
            st.write(df_cleaned)

            csv = df_cleaned.to_csv(index=False)
            st.download_button(
                label="Download mapped CSV",
                data=csv,
                file_name="mapped_legal_terms.csv",
                mime="text/csv",
            )

            st.markdown("""
            ### Next Steps
            Your cleaned and mapped data is ready! You can now:
            1. Use these Wikidata IDs in your systems or documents
            2. Explore the Wikidata pages for additional information
            3. Use this mapping for data integration projects
            """)

if __name__ == "__main__":
    main()
