# Cell 1: Setup
import streamlit as st
from openai import OpenAI
import os

# Get your OpenAI API key from environment variables 
api_key = os.getenv("OPENAI_API_KEY")  

# Used in production
client = OpenAI(api_key=api_key)

# Cell 2: Title & Description
st.title(':rainbow[Personalized Message Generator]')
st.subheader('🌱 🌼 🌿 🌻 ☘️ 🌺 🍀 🌸 🎍 🌷 🎋 💐 🍃 🌹 🌾')
st.subheader('🐝Bzz Bzz...🐝:rainbow[Hello there!] Allow me to help you craft a very special message for your loved one!', divider='rainbow')

# Cell 3: Function to generate text using OpenAI
def analyze_text(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    
    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    # Instructions for the AI (adjust if needed)
    messages = [
        {"role": "system", "content": " You are RuPaul, an amazing drag queen superstar here to spread positivity, inspiration, confidence, and love. Your job is to write a special message to a loved one. Please use a lot of colorful happy emojis in your response and keep it inspirational."},
        {"role": "user", "content": f" Please help me write a special message to a loved one based on the following:\n{text}"}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Lower temperature for less random responses
    )
    return response.choices[0].message.content


# Cell 4: Function to generate the image
def generate_image(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return

    response = client.images.generate(
        model="dall-e-3",
        prompt=text,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    # Assuming the API returns an image URL; adjust based on actual response structure
    return response.data[0].url

# Cell 5: Streamlit UI 
user_input = st.text_area("Enter a brief for your post:", "If you can't love yourself, how are you gonna love someone else??")

if st.button('☀️Inspire Me!!☀️'):
    with st.spinner('Generating...'):
        post_text = analyze_text(user_input)
        st.write(post_text)

    with st.spinner('Generating Sweet Image...'):
        thumbnail_url = generate_image(user_input)  # Consider adjusting the prompt for image generation if needed
        st.image(thumbnail_url, caption='What a fabulous image!')