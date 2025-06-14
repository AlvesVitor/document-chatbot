import streamlit as st
from utils import create_chain_talk, folder_files

def chat_window():
    st.header("🤖 Bem-vindo ao DocumentChatBot", divider=True)
    if not 'chain' in st.session_state:
        st.error("Faça o upload de arquivos para começar")
        st.stop()
    
    chain = st.session_state["chain"]
    memory = chain.memory 

    menssages = memory.load_memory_variables({})["chat_history"]
    container = st.container()
    for menssage in menssages:
        chat = container.chat_message(menssage.type)
        chat.markdown(menssage.content)
        
    new_menssage = st.chat_input("Converse com seus documentos")
    if new_menssage:
        chat = container.chat_message("human")
        chat.markdown(new_menssage)
        chat = container.chat_message("ai")
        chat.markdown("Gerando Resposta")
        chain.invoke({"question": new_menssage})
        st.rerun()

def save_uploaded_files(uploaded_files, folder):
    for file in folder.glob("*.csv"):
        file.unlink()

    for file in folder.glob("*.pdf"):
        file.unlink()
   
    for file in uploaded_files:
        (folder / file.name).write_bytes(file.read())

def main():
    with st.sidebar:
        st.header("Upload de CSV e PDF")
        uploaded_files = st.file_uploader("Adicione arquivos PDF ou CSV", 
                                         type=["csv", "pdf"], 
                                         accept_multiple_files=True)
        if uploaded_files:
            save_uploaded_files(uploaded_files, folder_files)
            st.success(f"{len(uploaded_files)} arquivo(s) salvo(s) com sucesso!")
        
        label_button = "Inicializar Chatbot"
        if "chain" in st.session_state:
            label_button = "Atualizar Chatbot"
        if st.button(label_button, use_container_width=True):
            if not any(folder_files.glob("*.csv")) and not any(folder_files.glob("*.pdf")):
                st.error("Adicione arquivos csv ou pdf para inicializar o chatbot")
            else:
                st.success("Inicializando o Chatbot...")
                create_chain_talk()
                st.rerun()
    chat_window()

if __name__ == "__main__":
    main()
