import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("이예선 전용 고민 상담소")

with st.form("form"):
    user_input = st.text_input("상담 질문")
    size = st.selectbox("Size", ["512x512", "256x256"])
    submit = st.form_submit_button("제출")

if submit and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the detail picture of the input. Response it shortly around 30 english words"
    }]

    gpt_prompt.append({
        "role": "user",
        "content": "a picture of peace of mind"
    })

    gpt_prompt2 = [{
        "role": "system",
        "content": "You are the best psychologist in the world, and if a patient asks a question, please answer so that he can find psychological stability. Please answer the question in Korean."
    }]

    gpt_prompt2.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )

        gpt_response2 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt2
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    prompt2 = gpt_response2["choices"][0]["message"]["content"]
    st.write(prompt2)
    st.write("이예선 사랑해💜")

    with st.spinner("Waiting for DALL-E..."):
        dalle_response = openai.Image.create(
            prompt=prompt,
            size=size
        )

    st.image(dalle_response["data"][0]["url"])

