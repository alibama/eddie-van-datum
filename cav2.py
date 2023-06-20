import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = st.secrets["OPENAI"]

# Define the quiz question and expected answer
question = "Explain the steps involved in calculating the net present value (NPV) of an investment project."
expected_answer = """
The steps involved in calculating the net present value (NPV) of an investment project are as follows:

1. Estimate the cash flows: Identify all the cash flows associated with the project, including initial investment, operating cash inflows, and terminal cash flows.

2. Determine the discount rate: Determine the appropriate discount rate to use for discounting the cash flows. The discount rate should reflect the project's risk and opportunity cost of capital.

3. Discount the cash flows: Apply the discount rate to each cash flow to calculate its present value. This is done by dividing each cash flow by (1 + discount rate) raised to the power of the corresponding period.

4. Sum the present values: Sum up the present values of all the cash flows to obtain the net present value.

5. Evaluate the NPV: If the NPV is positive, it indicates that the project is expected to generate more value than the initial investment and can be considered financially favorable. A negative NPV suggests that the project may not meet the required rate of return.

6. Consider other factors: While NPV is an important metric, it's essential to consider other factors such as strategic alignment, risk assessment, and qualitative aspects before making a final investment decision.

It's important to note that NPV analysis is based on several assumptions, and the accuracy of the results depends on the quality of the cash flow estimates and the discount rate chosen.
"""

# Generate critique using OpenAI's language model
def generate_critique(answer):
    prompt = f"Question: {question}\nAnswer: {answer}\nCritique:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    critique = response.choices[0].text.strip().split(":")[-1].strip()
#    critique = response.choices[0].text.strip().split("Critique:")[1].strip()
    return critique

# Streamlit app
def main():
    st.title("Investment Project NPV Quiz")
    st.write("Please provide a detailed answer to the following question:")

    # Display the quiz question
    st.subheader("Question:")
    st.write(question)

    # Get user's answer
    user_answer = st.text_area("Your Answer:", height=200)

    # Critique the user's answer
    if user_answer:
        critique = generate_critique(user_answer)
        st.subheader("Critique:")
        st.write(critique)
    #    rating = generate_rating(user_answer)
    #    st.subheader("Rating:")
    #    st.write(rating)


        # Provide feedback on the quality of the answer
    if user_answer.lower() == expected_answer.lower():
        st.write("✅ Your answer is acceptable!")
    else:
        st.write("❌ Your answer is not acceptable.")

# Run the app
if __name__ == "__main__":
    main()
