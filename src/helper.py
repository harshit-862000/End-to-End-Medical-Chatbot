from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from pathlib import Path


#Extract Data from the PDF file
#Extract Data from PDF file
def load_pdf_file(data):
    data_path = Path(data)
    candidate_paths = [
        data_path,
        Path.cwd() / data_path,
        Path.cwd().parent / data_path,
    ]
    resolved_path = next((path.resolve() for path in candidate_paths if path.exists()), None)

    if resolved_path is None:
        checked_paths = ", ".join(str(path.resolve()) for path in candidate_paths)
        raise FileNotFoundError(
            f"PDF directory not found. Create the folder and add PDF files there. Checked: {checked_paths}"
        )

    loader= DirectoryLoader(str(resolved_path), glob="*.pdf", loader_cls=PyPDFLoader)
    documents=loader.load()
    return documents



#split the data into chunks
#split and chunk the data
def text_splitter(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks

#download the embeddings from HuggingFace
#download embeddings from huggingface
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings





