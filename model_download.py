from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "EleutherAI/gpt-neo-125M"  # Replace with your correct model name

# Download the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Save them locally
tokenizer.save_pretrained("./gpt_neo_model/")
model.save_pretrained("./gpt_neo_model/")
