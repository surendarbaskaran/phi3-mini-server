import torch
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

# Check if CUDA (GPU) is available, otherwise use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
gpu_name = torch.cuda.get_device_name(0)
print(f"Model Loading to  in : {gpu_name}")

# Load the tokenizer and model from the local directory
try:
    tokenizer = AutoTokenizer.from_pretrained("./gpt_neo_model/")
    model = AutoModelForCausalLM.from_pretrained("./gpt_neo_model/").to(device)
    print("Model loaded to GPU ")
except Exception as e:
    app.logger.error(f"Failed to load model or tokenizer: {e}")
    tokenizer = None
    model = None

@app.route('/generate', methods=['POST'])
def generate():
    if not tokenizer or not model:
        return jsonify({'error': 'Model or tokenizer not loaded properly'}), 500

    data = request.json
    input_text = data.get('text', '')

    try:
        # Tokenize the input and move inputs to the GPU (if available)
        inputs = tokenizer(input_text, return_tensors="pt").to(device)

        # Generate response using the model on the GPU/CPU
        output = model.generate(**inputs, max_new_tokens=50)
        response_text = tokenizer.decode(output[0], skip_special_tokens=True)

        return jsonify({'response': response_text})
    except Exception as e:
        return jsonify({'error': f'Failed to generate response: {e}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'up'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
