import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Define the tax law question and expected answer
question = "What is the maximum annual contribution limit for a traditional IRA in 2023?"
expected_answer = "6000"

# Generate critique using OpenAI's language model
def generate_critique(response):
    prompt = f"Question: {question}\nAnswer: {response}\nCritique:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    critique = response.choices[0].text.strip().split(":")[-1].strip()
    return critique

# Streamlit app
def main():
    st.title("Tax Law Quiz")
    st.write("Please fill in the blank with the correct answer.")

    # Display the tax law question
    st.subheader("Question:")
    st.write(question)

    # Get user's response
    user_response = st.text_input("Your Answer:")

    # Critique the user's response
    if user_response:
        critique = generate_critique(user_response)
        st.subheader("Critique:")
        st.write(critique)

        # Provide feedback on correctness
        if user_response.lower() == expected_answer.lower():
            st.write("✅ Your answer is correct!")
        else:
            st.write("❌ Your answer is incorrect.")

# Run the app
if __name__ == "__main__":
    main()