# import openai
# import streamlit as st

# def ask_openai(question, max_tokens, temperature, top_p):
#     openai.api_type = "azure"
#     openai.api_version = "2024-02-01"
#     openai.api_base = 'https://appsmentalhealth.openai.azure.com/'  
#     openai.api_key = 'aa6cdeb6bb074332a4c71c3577c62421'  
    
#     try:
#         response = openai.ChatCompletion.create(
#             engine="appsmentalhealth",  
#             messages=st.session_state.messages,
#             max_tokens=max_tokens,
#             temperature=temperature,
#             top_p=top_p
#         )
#         if response["choices"][0]["message"]["content"]:
#             return response["choices"][0]["message"]["content"]
#         else:
#             return "Maaf, saya tidak yakin dengan pertanyaan Anda saat ini."
#     except openai.error.InvalidRequestError as e:
#         st.error(f"InvalidRequestError: {e}")
#         return "Maaf, terjadi kesalahan dalam memproses permintaan Anda."
#     except Exception as e:
#         st.error(f"An unexpected error occurred: {e}")
#         return "Maaf, terjadi kesalahan tak terduga."

# def main():
#     st.title("Chatbot Kesehatan Mental")

#     with st.sidebar:
#         st.header("Pengaturan")
#         max_tokens = st.slider("Max Tokens", min_value=10, max_value=500, value=150)
#         temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
#         top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=1.0)
#         clear_button = st.button("Hapus Riwayat Chat")

#     if clear_button:
#         st.session_state.messages = [{"role": "assistant", "content": "🤖 Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}]
#         st.experimental_rerun()

#     if "messages" not in st.session_state:
#         st.session_state.messages = [{"role": "assistant", "content": "🤖 Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}]

#     st.write(
#         """
#         <style>
#         .user-message {
#             text-align: right;
#             margin: 10px;
#         }
#         .bot-message {
#             text-align: left;
#             margin: 10px;
#         }
#         </style>
#         """, unsafe_allow_html=True
#     )

#     for msg in st.session_state.messages:
#         if msg["role"] == "user":
#             st.markdown(f"<div class='user-message'>👤 {msg['content']}</div>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<div class='bot-message'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

#     if prompt := st.chat_input():
#         st.session_state.messages.append({"role": "user", "content": prompt})
        
#         question = f"Anda adalah asisten kesehatan mental yang fokus pada informasi dan dukungan kesehatan mental, namun juga fleksibel dan interaktif untuk menjawab pertanyaan sehari-hari. Pengguna bertanya: {prompt}"
#         response = ask_openai(question, max_tokens, temperature, top_p)
#         st.session_state.messages.append({"role": "assistant", "content": f"🤖 {response}"})
#         st.experimental_rerun()

# if __name__ == "__main__":
#     main()

# import openai
# import streamlit as st

# def ask_openai(question, max_tokens, temperature, top_p):
#     openai.api_type = "azure"
#     openai.api_version = "2024-02-01"
#     openai.api_base = 'https://appsmentalhealth.openai.azure.com/'  
#     openai.api_key = 'aa6cdeb6bb074332a4c71c3577c62421'  
    
#     try:
#         response = openai.ChatCompletion.create(
#             engine="appsmentalhealth",  
#             messages=st.session_state.messages,
#             max_tokens=max_tokens,
#             temperature=temperature,
#             top_p=top_p
#         )
#         if response["choices"][0]["message"]["content"]:
#             return response["choices"][0]["message"]["content"]
#         else:
#             return "Maaf, saya tidak yakin dengan pertanyaan Anda saat ini."
#     except openai.error.InvalidRequestError as e:
#         st.error(f"InvalidRequestError: {e}")
#         return "Maaf, terjadi kesalahan dalam memproses permintaan Anda."
#     except Exception as e:
#         st.error(f"An unexpected error occurred: {e}")
#         return "Maaf, terjadi kesalahan tak terduga. Silahkan chat beberapa saat lagi"

# def main():
#     st.title("Chatbot Kesehatan Mental")

#     with st.sidebar:
#         st.header("Pengaturan")
#         max_tokens = st.slider("Max Tokens", min_value=10, max_value=500, value=450)
#         temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
#         top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=1.0)
#         clear_button = st.button("Hapus Riwayat Chat")

#     if clear_button:
#         st.session_state.messages = [
#             {
#                 "role": "system",
#                 "content": """
#                 Context: You are an AI assistant designed to help users gather information regarding Mental Health, with a focus on Mental Health only. Mental health information involves what is mental health, and why it's important to know regarding Mental Health issues. Users will input their questions, and you'll answer in Mental Health topics. DO NOT give user recommendations regarding medicine, you are NOT a doctor, you are willing to give recommendations to users for seeking professional advice.
#                 """
#             },
#             {"role": "assistant", "content": "🤖 Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}
#         ]
#         st.rerun()

#     if "messages" not in st.session_state:
#         st.session_state.messages = [
#             {
#                 "role": "system",
#                 "content": """
#                 Context: You are an AI assistant designed to help users gather information regarding Mental Health, with a focus on Mental Health only. Mental health information involves what is mental health, and why it's important to know regarding Mental Health issues. Users will input their questions, and you'll answer in Mental Health topics. DO NOT give user recommendations regarding medicine, you are NOT a doctor, you are willing to give recommendations to users for seeking professional advice.
#                 """
#             },
#             {"role": "assistant", "content": "🤖 Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}
#         ]

#     st.write(
#         """
#         <style>
#         .user-message {
#             text-align: right;
#             margin: 10px;
#         }
#         .bot-message {
#             text-align: left;
#             margin: 10px;
#         }
#         </style>
#         """, unsafe_allow_html=True
#     )

#     for msg in st.session_state.messages:
#         if msg["role"] != "system":
#             if msg["role"] == "user":
#                 st.markdown(f"<div class='user-message'>👤 {msg['content']}</div>", unsafe_allow_html=True)
#             else:
#                 st.markdown(f"<div class='bot-message'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

#     if prompt := st.chat_input():
#         st.session_state.messages.append({"role": "user", "content": prompt})
        
#         question = f"Pengguna bertanya: {prompt}"
#         response = ask_openai(question, max_tokens, temperature, top_p)
#         st.session_state.messages.append({"role": "assistant", "content": f"🤖 {response}"})
#         st.rerun()

# if __name__ == "__main__":
#     main()
        

# import openai
# import streamlit as st

# def ask_openai(question, max_tokens, temperature, top_p):
#     openai.api_type = "azure"
#     openai.api_version = "2024-02-01"
#     openai.api_base = 'https://appsmentalhealth.openai.azure.com/'  
#     openai.api_key = 'aa6cdeb6bb074332a4c71c3577c62421'  
    
#     response = openai.ChatCompletion.create(
#         engine="appsmentalhealth",  
#         messages=st.session_state.messages,
#         max_tokens=max_tokens,
#         temperature=temperature,
#         top_p=top_p
#     )

#     if response["choices"][0]["message"]["content"]:
#         return response["choices"][0]["message"]["content"]
#     else:
#         return "Maaf, saya tidak yakin dengan pertanyaan Anda saat ini."

# def main():
#     st.title("Chatbot Kesehatan Mental")

#     with st.sidebar:
#         st.header("Pengaturan")
#         max_tokens = st.slider("Max Tokens", min_value=10, max_value=500, value=150)
#         temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
#         top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=1.0)
#         clear_button = st.button("Hapus Riwayat Chat")

#     if clear_button:
#         st.session_state.messages = [
#             {
#                 "role": "system",
#                 "content": """
#                 Context: You are an AI assistant designed to help users gather information regarding Mental Health, with a focus on Mental Health only. Mental health information involves what is mental health, and why it's important to know regarding Mental Health issues. Users will input their questions, and you'll answer in Mental Health topics. DO NOT give user recommendations regarding medicine, you are NOT a doctor, you are willing to give recommendations to users for seeking professional advice.
#                 """
#             },
#             {"role": "assistant", "content": "🤖 Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}
#         ]
#         st.rerun()

#     if "messages" not in st.session_state:
#         st.session_state.messages = [
#             {
#                 "role": "system",
#                 "content": """
#                 Context: You are an AI assistant designed to help users gather information regarding Mental Health, with a focus on Mental Health only. Mental health information involves what is mental health, and why it's important to know regarding Mental Health issues. Users will input their questions, and you'll answer in Mental Health topics. DO NOT give user recommendations regarding medicine, you are NOT a doctor, you are willing to give recommendations to users for seeking professional advice.
#                 """
#             },
#             {"role": "assistant", "content": "🤖 Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}
#         ]

#     st.write(
#         """
#         <style>
#         .user-message {
#             text-align: right;
#             margin: 10px;
#         }
#         .bot-message {
#             text-align: left;
#             margin: 10px;
#         }
#         </style>
#         """, unsafe_allow_html=True
#     )

#     for msg in st.session_state.messages:
#         if msg["role"] != "system":
#             if msg["role"] == "user":
#                 st.markdown(f"<div class='user-message'>👤 {msg['content']}</div>", unsafe_allow_html=True)
#             else:
#                 st.markdown(f"<div class='bot-message'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

#     if prompt := st.chat_input():
#         st.session_state.messages.append({"role": "user", "content": prompt})
        
#         question = f"Pengguna bertanya: {prompt}"
#         response = ask_openai(question, max_tokens, temperature, top_p)
#         st.session_state.messages.append({"role": "assistant", "content": f"🤖 {response}"})
#         st.rerun()

# if __name__ == "__main__":
#     main()


# import openai
# from openai import AzureOpenAI
# import streamlit as st

# def ask_openai(question, max_tokens, temperature, top_p):

#     client = AzureOpenAI(
#         api_version="2024-02-01",
#         azure_endpoint="https://appsmentalhealth.openai.azure.com",
#         api_key='aa6cdeb6bb074332a4c71c3577c62421'
#     )
#     response = client.chat.completions.create(
#         model="appsmentalhealth", 
#         messages=st.session_state.messages,
#         max_tokens=max_tokens,
#         temperature=temperature,
#         top_p=top_p
#     )

#     if response.choices:
#         return response.choices[0].message["content"]
#     else:
#         return "Maaf, saya tidak yakin dengan pertanyaan Anda saat ini."

# def main():
#     st.title("Chatbot Kesehatan Mental")

#     with st.sidebar:
#         st.header("Pengaturan")
#         max_tokens = st.slider("Max Tokens", min_value=10, max_value=500, value=450)
#         temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
#         top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=1.0)
#         clear_button = st.button("Hapus Riwayat Chat")

#     if clear_button:
#         st.session_state.messages = [
#             {
#                 "role": "system",
#                 "content": """
#                 Context: You are an AI assistant designed to help users gather information regarding Mental Health, with a focus on Mental Health only. Mental health information involves what is mental health, and why it's important to know regarding Mental Health issues. Users will input their questions, and you'll answer in Mental Health topics. DO NOT give user recommendations regarding medicine, you are NOT a doctor, you are willing to give recommendations to users for seeking professional advice.
#                 """
#             },
#             {"role": "assistant", "content": "🤖 Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}
#         ]
#         st.rerun()

#     if "messages" not in st.session_state:
#         st.session_state.messages = [
#             {
#                 "role": "system",
#                 "content": """
#                 Context: You are an AI assistant designed to help users gather information regarding Mental Health, with a focus on Mental Health only. Mental health information involves what is mental health, and why it's important to know regarding Mental Health issues. Users will input their questions, and you'll answer in Mental Health topics. DO NOT give user recommendations regarding medicine, you are NOT a doctor, you are willing to give recommendations to users for seeking professional advice.
#                 """
#             },
#             {"role": "assistant", "content": "🤖 Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}
#         ]

#     st.write(
#         """
#         <style>
#         .user-message {
#             text-align: right;
#             margin: 10px;
#         }
#         .bot-message {
#             text-align: left;
#             margin: 10px;
#         }
#         </style>
#         """, unsafe_allow_html=True
#     )

#     for msg in st.session_state.messages:
#         if msg["role"] != "system":
#             if msg["role"] == "user":
#                 st.markdown(f"<div class='user-message'>👤 {msg['content']}</div>", unsafe_allow_html=True)
#             else:
#                 st.markdown(f"<div class='bot-message'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

#     if prompt := st.chat_input():
#         st.session_state.messages.append({"role": "user", "content": prompt})
        
#         question = f"Pengguna bertanya: {prompt}"
#         response = ask_openai(question, max_tokens, temperature, top_p)
#         st.session_state.messages.append({"role": "assistant", "content": f"🤖 {response}"})
#         st.rerun()

# if __name__ == "__main__":
#     main()


import openai
from openai import AzureOpenAI
import streamlit as st
import json

def ask_openai(question, max_tokens, temperature, top_p):
    client = AzureOpenAI(
        api_version="2024-02-01",
        azure_endpoint="https://appsmentalhealth.openai.azure.com",
        api_key='aa6cdeb6bb074332a4c71c3577c62421'
    )
    response = client.chat.completions.create(
        model="appsmentalhealth", 
        messages=st.session_state.messages,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p
    )

    response_json = json.loads(response.to_json())
    if response_json['choices']:
        return response_json['choices'][0]['message']['content']
    else:
        return "Maaf, saya tidak yakin dengan pertanyaan Anda saat ini."

def main():
    st.title("Chatbot Kesehatan Mental")

    with st.sidebar:
        st.header("Pengaturan")
        max_tokens = st.slider("Max Tokens", min_value=10, max_value=500, value=450)
        temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
        top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=1.0)
        clear_button = st.button("Hapus Riwayat Chat")

    if clear_button:
        st.session_state.messages = [
            {
                "role": "system",
                "content": """
                Context: You are an AI assistant designed to help users gather information regarding Mental Health, with a focus on Mental Health only. Mental health information involves what is mental health, and why it's important to know regarding Mental Health issues. Users will input their questions, and you'll answer in Mental Health topics. DO NOT give user recommendations regarding medicine, you are NOT a doctor, you are willing to give recommendations to users for seeking professional advice.
                """
            },
            {"role": "assistant", "content": "🤖 Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}
        ]
        st.rerun()

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": """
                Context: You are an AI assistant designed to help users gather information regarding Mental Health, with a focus on Mental Health only. Mental health information involves what is mental health, and why it's important to know regarding Mental Health issues. Users will input their questions, and you'll answer in Mental Health topics. DO NOT give user recommendations regarding medicine, you are NOT a doctor, you are willing to give recommendations to users for seeking professional advice.
                """
            },
            {"role": "assistant", "content": "🤖 Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}
        ]

    st.write(
        """
        <style>
        .user-message {
            text-align: right;
            margin: 10px;
        }
        .bot-message {
            text-align: left;
            margin: 10px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    for msg in st.session_state.messages:
        if msg["role"] != "system":
            if msg["role"] == "user":
                st.markdown(f"<div class='user-message'>👤 {msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='bot-message'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        question = f"Pengguna bertanya: {prompt}"
        response = ask_openai(question, max_tokens, temperature, top_p)
        st.session_state.messages.append({"role": "assistant", "content": f"🤖 {response}"})
        st.rerun()

if __name__ == "__main__":
    main()