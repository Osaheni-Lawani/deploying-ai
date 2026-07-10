import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def get_embedding(text):
    return embedding_model.encode(text).tolist()


def get_collection():

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="documents"
    )

    return collection


def load_documents():

    path = Path("documents/sample_docs.txt")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_database():

    collection = get_collection()

    if collection.count() == 0:

        document = load_documents()

        collection.add(
            ids=["doc1"],
            documents=[document],
            embeddings=[
                get_embedding(document)
            ]
        )

    return collection


def search_documents(query):

    collection = build_database()

    results = collection.query(
        query_embeddings=[
            get_embedding(query)
        ],
        n_results=1
    )

    return results["documents"][0][0]
