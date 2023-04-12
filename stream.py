import streamlit as st

def main():
    st.title("SEC Filing Information")

    company_name = st.text_input("Company Name")
    form_type = st.selectbox("Form Type", ["10-K", "10-Q", "8-K", "S-1"])
    filing_date = st.date_input("Filing Date")

    if form_type == "10-K":
        st.write("Additional Information:")
        fiscal_year_end = st.date_input("Fiscal Year End")
        company_size = st.selectbox("Company Size", ["Large Accelerated Filer", "Accelerated Filer", "Non-Accelerated Filer", "Smaller Reporting Company"])

    elif form_type == "10-Q":
        st.write("Additional Information:")
        quarter_end = st.date_input("Quarter End")

    elif form_type == "8-K":
        st.write("Additional Information:")
        event_type = st.selectbox("Event Type", ["Current Report", "Change in Fiscal Year End", "Other Event"])
        if event_type == "Other Event":
            event_description = st.text_input("Event Description")

    elif form_type == "S-1":
        st.write("Additional Information:")
        offering_amount = st.number_input("Offering Amount")
        use_of_proceeds = st.text_input("Use of Proceeds")

    if st.button("Submit"):
        st.write("Company Name: ", company_name)
        st.write("Form Type: ", form_type)
        st.write("Filing Date: ", filing_date)
        if form_type == "10-K":
            st.write("Fiscal Year End: ", fiscal_year_end)
            st.write("Company Size: ", company_size)
        elif form_type == "10-Q":
            st.write("Quarter End: ", quarter_end)
        elif form_type == "8-K":
            st.write("Event Type: ", event_type)
            if event_type == "Other Event":
                st.write("Event Description: ", event_description)
        elif form_type == "S-1":
            st.write("Offering Amount: ", offering_amount)
            st.write("Use of Proceeds: ", use_of_proceeds)

if __name__ == "__main__":
    main()
