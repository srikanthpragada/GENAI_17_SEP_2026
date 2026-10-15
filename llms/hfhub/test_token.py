from huggingface_hub import get_token
from huggingface_hub import constants

print(constants.HF_TOKEN_PATH)

token = get_token()
#print(token)
print("Saved or configured token found:", bool(token))
