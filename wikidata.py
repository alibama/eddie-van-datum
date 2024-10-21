import requests
import pandas as pd
import streamlit as st

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

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)

        if 'term' not in df.columns:
            st.error("The CSV file must contain a 'term' column.")
            return

        results = {}
        for term in df['term']:
            with st.expander(f"Map '{term}'"):
                wikidata_results = search_wikidata(term)
                if wikidata_results:
                    options = [f"{r['id']} - {r['label']} ({r['description']})" for r in wikidata_results]
                    selected = st.selectbox(f"Select the appropriate Wikidata entity for '{term}':", options + ['None of the above'])
                    if selected != 'None of the above':
                        results[term] = selected.split(' - ')[0]
                    else:
                        results[term] = ''
                else:
                    st.write("No results found.")
                    results[term] = ''

        df['wikidata_id'] = df['term'].map(results)

        st.write("Updated DataFrame:")
        st.write(df)

        csv = df.to_csv(index=False)
        st.download_button(
            label="Download mapped CSV",
            data=csv,
            file_name="mapped_legal_terms.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    main()