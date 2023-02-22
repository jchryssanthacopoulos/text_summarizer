import openai
import streamlit as st


def summarize(task, text):
    try:
        if task == "summary":
            augmented_prompt = (
                f"Below is a conversation between a client looking to rent an apartment, and a leasing agent helping to "
                "answer their questions. Can you provide a summary of the conversation?\n\n"
                f"{text}"
            )
        elif task == "rating":
            augmented_prompt = (
                f"Below is a conversation between a client looking to rent an apartment, and a leasing agent helping to "
                "answer their questions. Can you rate the quality of the agent's responses overall on a scale of 1 to 5?\n\n"
                f"{text}"
            )
        else:
            raise Exception("Invalid task type")

        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=1000,
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')
