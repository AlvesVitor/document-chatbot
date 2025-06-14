from pathlib import Path
import pandas as pd
from langchain_core.documents import Document
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai.chat_models import ChatOpenAI 
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
import streamlit as st
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

folder_files = Path(__file__).parent / "files"
model_name = "gpt-3.5-turbo-0125"

def import_files():
    docs = []
    
    # PDFs
    for file in folder_files.glob("*.pdf"):
        loader = PyPDFLoader(file)
        pdf_docs = loader.load()
        for doc in pdf_docs:
            doc.metadata["source"] = file.name
        docs.extend(pdf_docs)
    
    # CSVs
    for file in folder_files.glob("*.csv"):
        df = pd.read_csv(file)
        content = df.to_string(index=False)
        doc = Document(page_content=content, metadata={"source": file.name})
        docs.append(doc)

    return docs

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", ",", " "]
    )
    split_documents = splitter.split_documents(docs)
    for i, doc in enumerate(split_documents):
        doc.metadata["doc_id"] = i
    return split_documents

def create_vector_store(documentos):
    embedding_model = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(
        documents=documentos,
        embedding=embedding_model
    )
    return vector_store

def create_chain_talk():
    docs = import_files()
    docs = split_docs(docs)
    vector_store = create_vector_store(docs)

    chat = ChatOpenAI(model=model_name)
    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )
    retriever = vector_store.as_retriever()
    chat_chain = ConversationalRetrievalChain.from_llm(
        llm=chat,
        memory=memory,
        retriever=retriever,
        return_source_documents=True,
        verbose=True
    )
    st.session_state["chain"] = chat_chain
    return chat_chain
