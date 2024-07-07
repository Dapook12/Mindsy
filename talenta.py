# import openai
# from openai import AzureOpenAI
# import streamlit as st
# import json

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

#     response_json = json.loads(response.to_json())
#     if response_json['choices']:
#         return response_json['choices'][0]['message']['content']
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

def ask_openai(question):
    client = AzureOpenAI(
        api_version="2024-02-01",
        azure_endpoint="https://appsmentalhealth.openai.azure.com",
        api_key='aa6cdeb6bb074332a4c71c3577c62421'
    )
    response = client.chat.completions.create(
        model="appsmentalhealth", 
        messages=st.session_state.messages,
        max_tokens=450,  
        temperature=0.7, 
        top_p=1.0 
    )

    response_json = json.loads(response.to_json())
    if response_json['choices']:
        return response_json['choices'][0]['message']['content']
    else:
        return "Maaf, saya tidak yakin dengan pertanyaan Anda saat ini."

def append_call_center_info(response):
    # Daftar kata kunci yang akan memicu pesan arahan
    keywords = ["butuh bantuan", "membutuhkan bantuan", "hubungi profesional", "kesulitan", "krisis", "depresi", "bantuan segera", "obat", "diagnosa", "bunuh diri", "mati", "penyakit"]
    # Periksa apakah salah satu kata kunci ada dalam respons
    if any(keyword in response.lower() for keyword in keywords):
        response += "\n\nJika Anda membutuhkan bantuan segera, harap hubungi call center layanan kesehatan mental terdekat di 119 atau kunjungi pusat layanan kesehatan mental di kota Anda."
    return response

def main():
    st.title("Chatbot Kesehatan Mental")
        
    # Pop-up disclaimer saat pertama kali membuka aplikasi
    if "disclaimer_shown" not in st.session_state:
        st.session_state.disclaimer_shown = False
    if not st.session_state.disclaimer_shown:
        with st.modal("Disclaimer"):
            st.write(
                """
                <style>
                .disclaimer-content {
                    text-align: justify;
                    padding: 20px;
                    border-radius: 10px;
                    background-color: #f9f9f9;
                }
                </style>
                """, unsafe_allow_html=True
            )
            st.markdown(
                """
                <div class="disclaimer-content">
                <h3>Disclaimer</h3>
                <p>Platform ini hanya sebagai sarana edukasi belaka dan tidak akan menyediakan nasihat medis. Untuk bantuan medis profesional, silakan hubungi profesional kesehatan yang berlisensi atau penyedia layanan kesehatan.</p>
                <p>Klik tombol di bawah ini untuk melanjutkan.</p>
                </div>
                """, unsafe_allow_html=True
            )
            if st.button("Lanjutkan"):
                st.session_state.disclaimer_shown = True
            
    with st.sidebar:
        st.header("Pengaturan")
        clear_button = st.button("Hapus Riwayat Chat")

    if clear_button:
        st.session_state.messages = [
            {
                "role": "system",
                "content": """
                Context: You are an AI assistant named Mindsy designed to help users gather information regarding Mental Health, with a focus on Mental Health only. Mental health information involves what is mental health, and why it's important to know regarding Mental Health issues. Users will input their questions, and you'll answer in Mental Health topics. DO NOT give user recommendations regarding medicine, you are NOT a doctor, you are willing to give recommendations to users for seeking professional advice.
                """
            },
            {"role": "assistant", "content": "Disclaimer : Platform ini hanya bertujuan untuk edukasi belaka dan tidak akan menyediakan saran medis dalam bentuk apapun"},
            {"role": "assistant", "content": "Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}
        ]

    #     st.rerun()

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": """
                Context: You are an AI assistant named Mindsy designed to help users gather information regarding Mental Health, with a focus on Mental Health only. Mental health information involves what is mental health, and why it's important to know regarding Mental Health issues. Users will input their questions, and you'll answer in Mental Health topics. DO NOT give user recommendations regarding medicine, you are NOT a doctor, you are willing to give recommendations to users for seeking professional advice.
                """
            },
            {"role": "assistant", "content": "Disclaimer : Platform ini hanya bertujuan untuk edukasi belaka dan tidak akan menyediakan saran medis dalam bentuk apapun"},
            {"role": "assistant", "content": "Ada yang bisa saya bantu mengenai kesehatan mental hari ini?"}    
        ]

    st.write(
        """
        <style>
        .main-container {
            padding: 20px;
            border-radius: 10px;
        }
        .chat-container {
            max-width: 800px;
            margin: auto;
        }
        .user-message, .bot-message {
            padding: 10px 15px;
            margin: 10px 0;
            border-radius: 10px;
            max-width: 75%;
            width: fit-content;
            word-wrap: break-word;
        }
        .user-message {
            background-color: #DCF8C6;
            align-self: flex-end;
            text-align: right;
            float: right;
            clear: both;
        }
        .bot-message {
            background-color: #F1F0F0;
            align-self: flex-start;
            text-align: left;
            float: left;
            clear: both;
        }
        .username {
            font-weight: bold;
            margin-bottom: 5px;
            display: block;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    chat_container = st.container()

    with chat_container:
        chat_container.write(
            """
            <div class="chat-container">
            """, unsafe_allow_html=True
        )

        for msg in st.session_state.messages:
            if msg["role"] != "system":
                if msg["role"] == "user":
                    chat_container.markdown(
                        f"""
                        <div class='user-message'>
                            <div>{msg['content']}</div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                else:
                    chat_container.markdown(
                        f"""
                        <div class='bot-message'>
                            <span class='username'>Mindsy</span>
                            <div>{msg['content']}</div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
        
        chat_container.write(
            """
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        question = f"Pengguna bertanya: {prompt}"
        response = ask_openai(question)
        response_with_call_center_info = append_call_center_info(response)
        st.session_state.messages.append({"role": "assistant", "content": response_with_call_center_info})
        st.rerun()

if __name__ == "__main__":
    main()
