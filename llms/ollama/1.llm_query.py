from langchain_ollama import OllamaLLM
 
model = OllamaLLM(model="llama3.2:latest")
print(model.invoke("What is the capital of Spain?"))
#print(model.invoke("Who won IPL 2025"))
