# Run it from command prompt to print special chars 
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

loader = PyPDFLoader("../docs/courses_offered.pdf", mode='page')
docs = loader.load()
print("Loaded documents", len(docs))

# Split docs into chunks 
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, 
    chunk_overlap=50)

chunks = splitter.split_documents(docs)
print("No. of chunks :", len(chunks))

embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001")

vectorstore = Chroma.from_documents(chunks, embeddings_model)
retrieved_results = vectorstore.similarity_search("RAG", k = 2)

for result in retrieved_results:
    print(result.page_content)
    print("-" * 50)
    


