import maya.cmds as mpy  
 
 
class Textur_Replace():
    def __init__(self):
        pass


import os 



#检查文件目录是否存在  如果不存在就添加
def checkAndRemkir(_inPath):
    if os.path.exists(_inPath):
        return 
    else:
        if '.' in _inPath:
            _pathDir = os.path.split(_inPath)[0]
        else:
            _pathDir = _inPath 
            
        if  os.path.exists(_pathDir):
            return
        else:
            os.makedirs(_pathDir)  
            return              






    


