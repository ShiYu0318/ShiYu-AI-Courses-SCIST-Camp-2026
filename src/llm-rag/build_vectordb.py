import os
import logging
from dotenv import load_dotenv
from huggingface_hub import login

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    UnstructuredWordDocumentLoader,
)

from embeddings import EmbeddingGemmaEmbeddings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_PATH = os.path.join(BASE_DIR, "faiss_db")

CHUNK_SIZE = 300
CHUNK_OVERLAP = 50

LOADERS = {
    ".txt": TextLoader,
    ".pdf": PyPDFLoader,
    ".docx": UnstructuredWordDocumentLoader,
}


def main():
    load_dotenv()

    token = os.getenv("HUGGING_FACE_TOKEN")
    login(token=token)

    logging.basicConfig(level=logging.INFO)
    logging.info("Logged into Hugging Face Hub")

    documents = []

    for file in os.listdir(DATA_FOLDER):
        path = os.path.join(DATA_FOLDER, file)
        ext = os.path.splitext(file)[1]

        if ext not in LOADERS:
            continue

        logging.info("Loading %s ...", file)

        loader = LOADERS[ext](path)
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    split_docs = splitter.split_documents(documents)

    logging.info(
        "Split into %d chunks (chunk size=%d)",
        len(split_docs),
        CHUNK_SIZE,
    )

    embedding_model = EmbeddingGemmaEmbeddings()

    vectorstore = FAISS.from_documents(split_docs, embedding_model)
    vectorstore.save_local(OUTPUT_PATH)

    logging.info("Vectorstore saved to %s", OUTPUT_PATH)


if __name__ == "__main__":
    main()