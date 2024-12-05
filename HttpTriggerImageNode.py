import requests

class HttpTriggerImageNode:
  
  @classmethod
  def INPUT_TYPES(s): 
    return {
      "required": {        
        "input_image": ("IMAGE", {"forceInput": True}), 
        "http_url": ("STRING", {
                    "multiline": True, 
                    "default": ""}),
        "id": ("STRING", {
                    "multiline": True, 
                    "default": ""}),
        }
      }
  
  FUNCTION = "display_file_names"

  def display_file_names(self, input_image, http_url, id):
      # get请求一个接口，如果以http开头，则请求
      if http_url.startswith("http"):
        requests.get(http_url+id)
      print("http_url+id: " + http_url+id)
      return {"ui": {"string": [http_url+id,]}, "result": (http_url+id,)}
    
  RETURN_TYPES = ('STRING',)
  RETURN_NAMES = ('id',)
  OUTPUT_NODE = True
  
  CATEGORY = "Viva"