# Import necessary libraries and configure settings
import torch
import torchaudio
torch._dynamo.config.cache_size_limit = 64
torch._dynamo.config.suppress_errors = True
torch.set_float32_matmul_precision('high')

import ChatTTS
from IPython.display import Audio

# Initialize and load the model: 
chat = ChatTTS.Chat()
chat.load_models(compile=False) # Set to True for better performance

# Define the text input for inference (Support Batching)
texts = [
    "So we found being competitive and collaborative was a huge way of staying motivated towards our goals, so one person to call when you fall off, one person who gets you back on then one person to actually do the activity with.",
    ]

# Perform inference and play the generated audio
wavs = chat.infer(texts)
Audio(wavs[0], rate=24_000, autoplay=True)

torch.from_numpy(wavs[0])
# Save the generated audio 
# torchaudio.save("output.wav", torch.from_numpy(wavs[0]), 24000)


def askGPT(askPrompt):
    texts = [
    "So we found being competitive and collaborative was a huge way of staying motivated towards our goals, so one person to call when you fall off, one person who gets you back on then one person to actually do the activity with.",
    ]

    # Perform inference and play the generated audio
    texts.append(askPrompt)
    wavs = chat.infer(texts)
    Audio(wavs[0], rate=24_000, autoplay=True)
    return torch.from_numpy(wavs[0])
    


























# extra_body={
#     "data_sources": [
#         {
#             "type": "azure_search",
#             "parameters": {
#                 "endpoint": search_endpoint,
#                 "index_name": search_index,
#                 "authentication": {
#                     "type": "system_assigned_managed_identity"
#                 }
#             }
#         }
#     ]
# }