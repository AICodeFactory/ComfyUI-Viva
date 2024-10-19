__VERSION__ = "0.6.0"

import os, sys, filecmp, shutil, __main__
python = sys.executable


#INPORT NODES
from .HttpTriggerNode import HttpTriggerNode

# ------- MAPPING ------- #
NODE_CLASS_MAPPINGS = { 
    "HttpTrigger_Viva": HttpTriggerNode,
}

NODE_DISPLAY_NAME_MAPPINGS = { 
    "HttpTrigger_Viva": "HttpTrigger (Viva)",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
