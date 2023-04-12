import streamlit as st

def main():
    st.title("SEC Filing Information")

    company_name = st.text_input("Company Name")
    form_type = st.selectbox("Form Type", ["10-K", "10-Q", "8-K", "S-1"])
    filing_date = st.date_input("Filing Date")

    if form_type == "8-K":
        st.write("Additional Information:")
        event_type = st.selectbox("Event Type", ["Current Report", "Change in Fiscal Year End", "Other Event"])
        if event_type == "Other Event":
            event_description = st.text_input("Event Description")

    if st.button("Submit"):
        st.write("Company Name: ", company_name)
        st.write("Form Type: ", form_type)
        st.write("Filing Date: ", filing_date)
        if form_type == "8-K":
            st.write("Event Type: ", event_type)
            if event_type == "Other Event":
                st.write("Event Description: ", event_description)

if __name__ == "__main__":
    main()
