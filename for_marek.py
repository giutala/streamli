import streamlit as st
import random

def generate_hearts(num_hearts):
    hearts = ["❤️", "💙", "💚", "💛", "💜", "🧡"]
    return [random.choice(hearts) for _ in range(num_hearts)]

def main():
    st.title("Open when needed. With love, giugiu.")

    if st.toggle("Activate sad marek"):
        num_hearts = st.slider("How sad are you?", min_value=1, max_value=100, value=5)
        hearts = generate_hearts(num_hearts)

        for heart in hearts:
            st.title(heart)

if __name__ == "__main__":
    main()
