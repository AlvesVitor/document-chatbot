# 🧠 Document Chatbot - OpenAI

Este projeto implementa um chatbot que responde a perguntas com base em documentos nos formatos PDF e CSV. A aplicação utiliza o modelo de linguagem `gpt-3.5-turbo` da OpenAI e o conceito de **Retrieval-Augmented Generation (RAG)** para fornecer respostas precisas e contextuais.

## 📑 Funcionalidades

- Processamento de arquivos `.pdf` e `.csv`.
- Respostas baseadas em conteúdo extraído dos documentos.
- Interface interativa desenvolvida com Streamlit.
- Integração com embeddings e busca vetorial via FAISS.

## 📂 Estrutura do Projeto

O projeto espera uma pasta chamada `files/` na raiz do repositório, onde os arquivos `.pdf` ou `.csv` devem ser armazenados. Essa pasta será criada automaticamente caso não exista.

```
├── app.py              # Arquivo principal da aplicação
├── files/              # Pasta para armazenar documentos
├── requirements.txt    # Dependências do projeto
├── .env                # Variáveis de ambiente (ex.: API key)
└── README.md           # Documentação do projeto
```

## 🛠️ Requisitos

- **Python**: 3.8 ou superior
- **Pip**: Gerenciador de pacotes do Python
- **Chave de API da OpenAI**: Necessária para utilizar o modelo `gpt-3.5-turbo`

### Bibliotecas Utilizadas

- `langchain`
- `langchain-community`
- `langchain-openai`
- `openai`
- `pypdf`
- `pandas`
- `streamlit`
- `python-dotenv`
- `faiss-cpu`

## 📦 Instalação

Siga os passos abaixo para configurar e executar o projeto:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/AlvesVitor/document-chatbot.git
   cd document-chatbot
   ```

2. **Crie um ambiente virtual** (recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:

   - Crie um arquivo `.env` na raiz do projeto.
   - Adicione sua chave de API da OpenAI:
     ```
     OPENAI_API_KEY=sua-chave-aqui
     ```

5. **Execute a aplicação**:

   ```bash
   streamlit run app.py
   ```

   A interface será aberta automaticamente no seu navegador padrão.

## 🚀 Uso

1. Coloque os arquivos `.pdf` ou `.csv` na pasta `files/`.
2. Acesse a interface do Streamlit no navegador.
3. Faça perguntas relacionadas ao conteúdo dos documentos, e o chatbot responderá com base nas informações processadas.

## 📝 Notas

- Certifique-se de que os arquivos na pasta `files/` são legíveis e estão no formato correto.
- O desempenho do chatbot pode variar dependendo do tamanho e da complexidade dos documentos.
- Para melhores resultados, utilize documentos bem estruturados.

## 👨‍💻 Desenvolvedor

Desenvolvido por Vitor Luis Alves.
