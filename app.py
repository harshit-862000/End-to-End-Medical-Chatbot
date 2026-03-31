from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI  # CHANGED: from OpenAI to ChatOpenAI
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__, template_folder="template")

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")  # ADDED: Get OpenRouter key

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

embeddings = download_hugging_face_embeddings()

index_name = "medicalbot"

# Embed each chunk and upsert the embeddings into pinecone
docsearch = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# CHANGED: Configure for OpenRouter
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.4,
    max_tokens=500
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answering_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answering_chain)    


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    try:
        msg = request.form.get("msg", "")
        
        if not msg:
            return jsonify({"error": "No message provided"}), 400
        
        print(f"Received message: {msg}")
        
        response = rag_chain.invoke({"input": msg})
        
        print(f"Response: {response.get('answer', 'No answer')}")
        
        answer = response.get("answer", "I'm sorry, I couldn't generate a response.")
        return str(answer)
    
    except Exception as e:
        print(f"Error in /get endpoint: {str(e)}")
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)