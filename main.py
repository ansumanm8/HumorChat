import streamlit as st
from humorchatbot import generate_humorous_response


def main():
    st.set_page_config(
        page_title="Humor Chat",
        layout="centered",
        page_icon='🤖'
    )

    st.header("Humor ChatBot! \n [ OpenAI-GPT-3.5-turbo-instruct ]")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(name=message["role"], avatar=message["avatar"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Want to know! How funny I am ask me anything..."):
        # Display user message in chat message container
        user_avatar = './assets/user_avatar.jpg'
        bot_avatar = './assets/chad_test.webp'
        st.chat_message("user", avatar=user_avatar).markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user","avatar": user_avatar, "content": prompt})

        
        # Display assistant response in chat message container
        with st.chat_message("assistant", avatar=bot_avatar):
            with st.spinner("Thinking.."):
                response = generate_humorous_response(prompt)
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant","avatar": bot_avatar, "content": response})

if __name__ == '__main__':
    main()