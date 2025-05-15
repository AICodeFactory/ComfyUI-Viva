import requests
from .AlwaysEqualProxy import AlwaysEqualProxy
from server import PromptServer

any_type = AlwaysEqualProxy("*")

class HttpTriggerCommonNode:
  
  @classmethod
  def INPUT_TYPES(s):
        return {"required": {"http_url": ("STRING", { "multiline": True, "default": ""}),}, 
                "optional": {"anything": (any_type, {}), }}
  
  RETURN_TYPES = (any_type,)
  RETURN_NAMES = ('output',)
  INPUT_IS_LIST = True
  OUTPUT_NODE = True
  FUNCTION = "http_trigger"
  CATEGORY = "Viva"

  def http_trigger(self, http_url):
      print( http_url)
      # get请求一个接口
      requests.get(http_url)
      return {"ui": {"string": [prompt_id]}, "result": (prompt_id)}
    