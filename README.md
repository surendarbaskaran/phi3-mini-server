# phi3-mini-server
This project is basically to use Phi3-mini model (developed by Microsoft ) with API, I have added my system configurations in below tab

## Dependencies:
* Flash
* Transformers

## Steps to Run the Application
  Execute the below commands 
  * pip install Flask Transformer
  * python app.py
  * In terminal [CMD or VScode] \
    
      curl http://localhost:8080/health \
    
      the correct response should be  {"status":"up"} \
    
      curl -X POST http://localhost:8080/generate -H "Content-Type: application/json" -d "{\"text\": \"Once upon a time\"}" \
    
      The response will be {'response': 'response text from phi3-mini' }

## Output
when I tried to hit the URL , response took more than 20 mins

![image](https://github.com/user-attachments/assets/22f94e60-4e63-45cf-8993-25b98b8fe548)


In the below image, It can be seen health response as "UP"

![image](https://github.com/user-attachments/assets/7274a057-ec22-49a4-ac9e-ae8d42f66463)

so try loading the model in GPU

## System Config
* I 5-11400H
* 16 GB RAM, (Suggest you to use minimum of 32 GB for getting faster output, 100% hit with 16 GB ram)
* GTX 1650-Max-Q Design
