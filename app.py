import requests
import xml.etree.ElementTree as ET
import pandas as pd
import streamlit as st
from itertools import groupby

def get_publications_for_institution(institution):
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=AFF:\"{institution}\"&resulttype=core&pageSize=1000"
    response = requests.get(url)
    root = ET.fromstring(response.content)
    publications = []
    for result in root.iter("result"):
        departments = []
        for affiliation in result.iter("affiliation"):
            department = affiliation.find("department")
            if department is not None:
                departments.append(department.text)
        publications.append({"title": result.find("title").text, "departments": departments})
    return publications

def group_departments(departments):
    def keyfunc(x):
        return "".join(c for c in x.lower() if c.isalnum())
    sorted_departments = sorted(departments, key=keyfunc)
    grouped_departments = []
    for _, g in groupby(sorted_departments, key=keyfunc):
        grouped_departments.append(list(g))
    return grouped_departments

st.title("Europe PMC Institution Query App")

institution = st.text_input("Enter the name of an institution:", "Harvard University")
publications = get_publications_for_institution(institution)

if not publications:
    st.write("No publications found for this institution.")
else:
    department_lists = [publication["departments"] for publication in publications]
    departments = [department for department_list in department_lists for department in department_list]
    grouped_departments = group_departments(departments)
    
    st.write(f"Found {len(publications)} publications for {institution}")
    st.write(f"Found {len(departments)} departments:")
    for department_group in grouped_departments:
        st.write(f"- {', '.join(department_group)}")
