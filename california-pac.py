import streamlit as st

# Function to check if user has made a donation in the past year
def has_donated(user_id):
    # Code to query database and check if user has made a donation in the past year
    # Returns True or False
    pass

# Define required thresholds
CONTRIBUTION_THRESHOLD = 2000
MULTIPURPOSE_THRESHOLD_1YR = 50000
MULTIPURPOSE_THRESHOLD_4YR = 100000
IE_THRESHOLD = 1000
MAJOR_DONOR_THRESHOLD = 10000
DONOR_DISCLOSURE_THRESHOLD = 100

# Main function to run the Streamlit app
def main():
    st.title('PAC Status and Disclosure Requirements')
    
    # User input for ID and donation information
    user_id = st.text_input('Enter your user ID:')
    donation_status = has_donated(user_id)
    
    # PAC status determination
    st.header('PAC Status Determination')
    st.write('California does not impose a major or primary purpose test for PAC status.')
    st.write('In general, the definition of a "committee" is based solely on receiving/making "contributions" and making "independent expenditures."')
    st.write('An organization must register as a recipient committee upon receiving $2,000 in contributions in a calendar year, or if a multipurpose organization, upon making contributions or expenditures in excess of $50,000 in a one-year period or $100,000 in a consecutive four-year period.')
    st.write('An "independent expenditure committee" is required to report after making IEs totaling more than $1,000 during a calendar year.')
    st.write('A "major donor committee" is required to report after making contributions totaling more than $10,000 during a calendar year.')
    
    # Required disclosures and error checking
    st.header('Required Disclosures and Error Checking')
    if donation_status:
        st.write('You have made a donation in the past year and are required to disclose your donor information.')
    else:
        st.write('You have not made a donation in the past year.')
    
    if st.button('Check Contribution Threshold'):
        if donation_status and CONTRIUBTION_THRESHOLD <= 0:
            st.write('Error: You have already reached the contribution threshold for this calendar year.')
        elif not donation_status and CONTRIUBTION_THRESHOLD > 0:
            st.write(f'You need to make a contribution of at least ${CONTRIBUTION_THRESHOLD} to meet the contribution threshold for this calendar year.')
        else:
            st.write('You have already met the contribution threshold for this calendar year.')
    
    if st.button('Check Multipurpose Organization Threshold'):
        if donation_status and (MULTIPURPOSE_THRESHOLD_1YR <= 0 or MULTIPURPOSE_THRESHOLD_4YR <= 0):
            st.write('Error: You have already reached the multipurpose organization threshold for this period.')
        elif not donation_status and (MULTIPURPOSE_THRESHOLD_1YR > 0 or MULTIPURPOSE_THRESHOLD_4YR > 0):
            st.write(f'You need to make a contribution or expenditure of at least ${MULTIPURPOSE_THRESHOLD_1YR} in a one-year period or ${MULTIPURPOSE_THRESHOLD_4YR} in a consecutive four-year period to meet the multipurpose organization threshold.')
        else:
            st.write('You have already met the multipurpose organization threshold.')
    
    if st.button('Check Independent Expenditure Threshold'):
        if donation_status and