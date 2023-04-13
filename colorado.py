import streamlit as st
import pandas as pd

# Define the title and subtitle of the app
st.title("Campaign Donation Tracker")
st.subheader("Requirements for Campaign Donations")

# Define the content of the app
st.header("Donor Disclosure")
st.write("Donors who contribute more than $100 in a calendar year must be disclosed.")
st.write("Campaign committees must register with the appropriate regulatory agency if they receive contributions in excess of $3,000 in a calendar year.")

# Define the campaign donation form
st.header("Campaign Donation Form")
donor_name = st.text_input("Donor Name")
donor_address = st.text_input("Donor Address")
donation_amount = st.number_input("Donation Amount", min_value=0, step=1)

# Define the campaign donations table
st.header("Campaign Donations")
campaign_donations = pd.DataFrame(columns=["Name", "Address", "Amount"])
if st.button("Add Donation"):
    campaign_donations = campaign_donations.append({"Name": donor_name, "Address": donor_address, "Amount": donation_amount}, ignore_index=True)
st.dataframe(campaign_donations)

# Define the donor disclosure table
st.header("Donor Disclosure")
if campaign_donations.empty:
    st.write("No donations yet.")
else:
    donor_disclosures = campaign_donations[campaign_donations["Amount"] > 100]
    if len(donor_disclosures) == 0:
        st.write("No donors meet disclosure requirements.")
    else:
        st.write("Donors who contributed more than $100:")
        st.dataframe(donor_disclosures)

# Check whether campaign committee needs to register
if campaign_donations["Amount"].sum() > 3000:
    st.warning("Campaign committee must register with the regulatory agency.")
