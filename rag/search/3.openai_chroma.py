# install chorma using - pip install langchain_chroma 

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

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

vectorstore = Chroma.from_texts(documents, embeddings_model)

query = "Football"
results = vectorstore.similarity_search(query, k=2)  # Get the top 3 results

for doc in results:
    print(doc.page_content)
    print('-' * 50)
