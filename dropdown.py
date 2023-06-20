import streamlit as st
import openai

# Set up your OpenAI API credentials
openai.api_key = st.secrets["OPENAI"]

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

    if user_idea:
        # Generate response praising the idea
        positive_prompt = f"Your idea on managing rising housing costs: {user_idea}\n\nResponse:"
        positive_response = get_openai_response(positive_prompt, temperature=0.2)

        st.write("Positive Response:")
        st.write(positive_response)

        # Generate response criticizing the idea
        negative_prompt = f"Your idea on managing rising housing costs: {user_idea}\n\nResponse:"
        negative_response = get_openai_response(negative_prompt, temperature=0.8)

        st.write("Negative Response:")
        st.write(negative_response)

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
