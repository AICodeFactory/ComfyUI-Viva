__VERSION__ = "0.6.0"

import os, sys, filecmp, shutil, __main__
python = sys.executable


#INPORT NODES
from .HttpTriggerImageNode import HttpTriggerImageNode
from .HttpTriggerVivaNode import HttpTriggerVivaNode

# ------- MAPPING ------- #
NODE_CLASS_MAPPINGS = { 
    "HttpTrigger_Viva": HttpTriggerVivaNode,
    "HttpTrigger_Image": HttpTriggerImageNode
}

NODE_DISPLAY_NAME_MAPPINGS = { 
    "HttpTrigger_Viva": "HttpTrigger (Viva)",
    "HttpTrigger_Image": "HttpTrigger (Image)",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
