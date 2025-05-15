import requests
from .AlwaysEqualProxy import AlwaysEqualProxy

any_type = AlwaysEqualProxy("*")

class HttpTriggerCommonNode:
  
  @classmethod
  def INPUT_TYPES(s):
        return {"required": {"http_url": ("STRING", { "multiline": True, "default": ""}),}, 
                "optional": {"anything": (any_type, {}), },
                "hidden": {"prompt": "PROMPT", "dynamic_prompt": "DYNPROMPT"}}
  
  RETURN_TYPES = (any_type,)
  RETURN_NAMES = ('output',)
  INPUT_IS_LIST = True
  OUTPUT_NODE = True
  FUNCTION = "http_trigger"
  CATEGORY = "Viva"

  def http_trigger(self, http_url, prompt=None, dynamic_prompt=None, anything=None):
      # get请求一个接口
      requests.get(http_url)
      return {"ui": {"string": [http_url]}, "result": (http_url)}
    