import streamlit as st

# Define the donation threshold for disclosure
DISCLOSURE_THRESHOLD = 100

def main():
    # Set the page title
    st.set_page_config(page_title="California Donor Disclosure App")
    
    # Define the form inputs
    name = st.text_input("Name")
    address = st.text_input("Address")
    occupation = st.text_input("Occupation")
    employer = st.text_input("Employer")
    donation_amount = st.number_input("Donation Amount", value=0, min_value=0, step=1)
    
    # Calculate the disclosure amount based on the user's donation
    if donation_amount >= DISCLOSURE_THRESHOLD:
        disclosure_amount = donation_amount
    else:
        disclosure_amount = 0
        
    # Determine if the donation is designated, restricted, or prohibited from being used for political contributions or expenditures in connection with California state and local elections
    is_designated = st.checkbox("My donation is designated, restricted, or prohibited from being used for political contributions or expenditures in connection with California state and local elections.")
    
    # Determine if disclosure is required based on the user's donation and designation status
    if disclosure_amount > 0 and not is_designated:
        disclosure_required = True
    else:
        disclosure_required = False
    
    # Display the user's disclosure requirements
    if disclosure_required:
        st.write("Based on your donation, you are required to disclose your name, address, occupation, employer, and the amount of your donation.")
    else:
        st.write("Based on your donation, disclosure is not required.")
        
if __name__ == '__main__':
    main()