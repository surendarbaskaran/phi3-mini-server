> # phi3-mini-server
This project is basically to use LLM model with API, I have added my system configurations in below tab.  Below are the list of model I tried to mount
*  Phi3-mini (status : Failed) unable to run in my config
*  EleutherAI/gpt-neo-125M (status : Success)

> ## Dependencies:
* Flask
* Transformers
* Torch

> ## Files :
* GPU_checker.py \
    This file can be used to check cuda installed version and test GPU can be accessed by cuda
* gpu_app.py \
    Used to load the model from transformer library directly without downloading. 
* model_download.py \
    This is used to copy the model to offline device , replace the model name variable with required model name and path  to save the model.
* offline_model_load.py \
    Used to load the model from offline path. Need to replace  model stored path. 


> ## Steps to Run the Application
  Execute the below commands 
  * pip install Flask Transformer torch
  * python app.py
  * In terminal [CMD or VScode] \
    
      curl http://localhost:8080/health \
    
      the correct response should be  {"status":"up"} \
    
      curl -X POST http://localhost:8080/generate -H "Content-Type: application/json" -d "{\"text\": \"Once upon a time\"}" \
    
      The response will be {'response': 'response text from model' }


> ## Output
### Phi 3 - Mini (Failed)
when I tried to hit the URL , response took more than 20 mins and model cannot be loaded into GPU because GTX 1650 has only 4 gb while model required 12 GB 

![image](https://github.com/user-attachments/assets/22f94e60-4e63-45cf-8993-25b98b8fe548)


In the below image, It can be seen health response as "UP"

![image](https://github.com/user-attachments/assets/7274a057-ec22-49a4-ac9e-ae8d42f66463)

### EleutherAI/gpt-neo-125M 

since the model size is 480 mb, it worked both with CPU and GPU , but it needs to trained on personal data.

![image](https://github.com/user-attachments/assets/832a95cc-946e-46b1-a241-fe2ebb5807b4)

![image](https://github.com/user-attachments/assets/c2f6ce9f-ecad-4017-b64f-7718ccbe5afe)



> ## System Config
* I 5-11400H
* 16 GB RAM
* GTX 1650-Max-Q Design
