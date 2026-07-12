from dotenv import load_dotenv
load_dotenv(".secrets")

import chromadb
from sentence_transformers import SentenceTransformer

from utils.clients import get_client
from assignment_chat.prompts import build_prompt
from assignment_chat.guardrails import validate_input, validate_output

# Embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Chroma database
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

client = chromadb.PersistentClient(
    path=str(BASE_DIR / "chroma_db")
)

collection = client.get_or_create_collection(
    name="documents"
)

# OpenAI gateway client
llm_client = get_client(use_gateway=True)


def retrieve_context(question, n_results=3):

    question_embedding = embedding_model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )

    documents = results["documents"][0]

    return "\n\n".join(documents)



def answer_question(question, history=None):

    valid, message = validate_input(question)

    if not valid:
        return message

    context = retrieve_context(question)

    prompt = build_prompt(
        context,
        question
    )

    response = llm_client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return validate_output(response.output_text)
    
      
