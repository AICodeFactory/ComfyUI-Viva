import requests

class HttpTriggerImageNode:
  
  @classmethod
  def INPUT_TYPES(s): 
    return {
      "required": {
        "http_url": ("STRING", {
                    "multiline": True, 
                    "default": ""}),
        "id": ("STRING", {
                    "multiline": True, 
                    "default": ""}),
        },
        "optional": {
           "input_image": ("IMAGE", {}),
           "file_names": ("VHS_FILENAMES", {}), 
           "input_string": ("STRING", {})
        }
      }
  
  FUNCTION = "display_file_names"

  def display_file_names(self, file_names, http_url, id):
      # get请求一个接口
      requests.get(http_url+id)
      print("http_url+id: " + http_url+id)
      return {"ui": {"string": [http_url+id,]}, "result": (http_url+id,)}
    
  RETURN_TYPES = ('STRING',)
  RETURN_NAMES = ('id',)
  OUTPUT_NODE = True
  
  CATEGORY = "Viva"