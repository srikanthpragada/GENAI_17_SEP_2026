from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import os 

embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

documents = [
    "Liverpool is winning a lot of matches",
    "Ollama allows running LLMs locally.",
    "Manchester City is doing awesome!",
    "Bill Gates Founded Microsoft",
    "Real Madrid won UEFA Champions League 13 times."
 ]

folder_path = "./courses"
if not os.path.exists(folder_path):
    vectorstore = Chroma.from_texts(
                                texts = documents, 
                                embedding=embeddings_model,
                                collection_name="courses",
                                persist_directory="./courses")
    print("Created embeddings..")
else:
    vectorstore = Chroma(
        collection_name="courses",
        embedding_function=embeddings_model,
        persist_directory="./courses")
    print("Loaded embeddings..")

