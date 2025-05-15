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
      print(f"http_url: {http_url}")
      # 处理列表类型的http_url
      for url in http_url:
          # 如果url不为空，且以http://或https://开头，则get请求一个接口
          if url and isinstance(url, str) and url.strip() and url.strip().startswith(("http://", "https://")):
              response = requests.get(url.strip())
              print(f"response: {response.text}")
      return {"ui": {"string": http_url}, "result": (http_url)}
    