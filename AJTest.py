from model import ExLlama, ExLlamaCache, ExLlamaConfig
from tokenizer import ExLlamaTokenizer
from generator import ExLlamaGenerator
import os, glob

# Directory containing model, tokenizer, generator

model_directory =  "C:/Users/oncho/Documents/code/localai/oobabooga_windows/text-generation-webui/models/WizardLM-33B-V1.0-Uncensored-GPTQ"

# Locate files we need within that directory

tokenizer_path = os.path.join(model_directory, "tokenizer.model")
model_config_path = os.path.join(model_directory, "config.json")
st_pattern = os.path.join(model_directory, "*.safetensors")
model_path = glob.glob(st_pattern)[0]

# Create config, model, tokenizer and generator

config = ExLlamaConfig(model_config_path)               # create config from config.json
config.model_path = model_path                          # supply path to model weights file

model = ExLlama(config)                                 # create ExLlama instance and load the weights
tokenizer = ExLlamaTokenizer(tokenizer_path)            # create tokenizer from tokenizer model file

cache = ExLlamaCache(model)                             # create cache for inference
generator = ExLlamaGenerator(model, tokenizer, cache)   # create generator

# Configure generator

generator.disallow_tokens([tokenizer.eos_token_id])

generator.settings.token_repetition_penalty_max = 1.2
generator.settings.temperature = 0.95
generator.settings.top_p = 0.65
generator.settings.top_k = 100
generator.settings.typical = 0.5

# Produce a simple generation

#prompt = "Once upon a time,"
prompt = "USER: I need to plan my vacation to Bali. I think I'll go there in november and come back in december or something like that. Give me a complete markdown document detailing a plan for my trip and any other information you think I might need.\nASSISTANT:"
print (prompt, end = "")

output = generator.generate_simple(prompt, max_new_tokens = 1000)

print(output[len(prompt):])
