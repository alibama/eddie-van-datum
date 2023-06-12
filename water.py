import streamlit as st

def calculate_flow_rate(pipe_size):
    # Placeholder function to calculate flow rate based on pipe size
    # Replace with your own logic or calculations
    return pipe_size * 2.5

def main():
    st.title("Water Volume Flow in Pipes")

    pipe_size = st.slider("Select Pipe Size (inches)", min_value=1, max_value=10)
    flow_rate = calculate_flow_rate(pipe_size)

    st.write(f"Pipe Size: {pipe_size} inches")
    st.write(f"Flow Rate: {flow_rate} gallons per minute")

if __name__ == "__main__":
    main()
