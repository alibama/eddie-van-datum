import streamlit as st
import openai

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

def get_openai_response(prompt, temperature):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=temperature,
        n=1,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        best_of=1
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("Managing Rising Housing Costs")
    st.write("Please provide your idea on how to manage rising housing costs:")

    user_idea = st.text_area("Your Idea")

    response_type = st.selectbox("Choose the response type:", ("Positive", "Negative"))

    if user_idea:
        if response_type == "Positive":
            # Generate response praising the idea
            prompt = f"Your idea on managing rising housing costs: {user_idea}\n\nResponse:"
            temperature = 0.2
        else:
            # Generate response criticizing the idea
            prompt = f"Your idea on managing rising housing costs: {user_idea}\n\nResponse:"
            temperature = 0.8

        response = get_openai_response(prompt, temperature)

        st.write("Response:")
        st.write(response)

        # Generate a suggested compromise from the user's idea
        compromise_prompt = f"Your idea on managing rising housing costs: {user_idea}\n\nSuggested Compromise:"
        compromise_response = get_openai_response(compromise_prompt, temperature=0.5)

        st.write("Suggested Compromise:")
        st.write(compromise_response)

        # Gather feedback on whether the information provided changed the user's mind
        feedback = st.radio(
            "Did the information provided change your mind about your position?",
            ("Yes", "No")
        )

        if feedback == "Yes":
            st.write("We appreciate your openness to consider different perspectives.")
        else:
            st.write("Thank you for sharing your thoughts.")

if __name__ == '__main__':
    main()
