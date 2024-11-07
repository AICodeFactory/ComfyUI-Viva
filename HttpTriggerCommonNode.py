import requests

class HttpTriggerCommonNode:
  
  @classmethod
  def INPUT_TYPES(s):
        return {"required": {"http_url": ("STRING", { "multiline": True, "default": ""}),}, 
                "optional": {"anything": (any_type, {}), },
                "hidden": {"prompt": "PROMPT", }}
  
  RETURN_TYPES = (any_type,)
  RETURN_NAMES = ('output',)
  INPUT_IS_LIST = True
  OUTPUT_NODE = True
  FUNCTION = "http_trigger"
  CATEGORY = "Viva"

  def http_trigger(self, http_url, prompt=None, **kwargs):
      # get请求一个接口
      # requests.get(http_url)
      print("http_url: " + http_url)
      print("prompt: " + prompt)
      return {"ui": {"string": [http_url]}, "result": (http_url)}
    