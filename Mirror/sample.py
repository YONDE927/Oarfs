from pathlib import Path
import time

class Mypath():
    def __init__(self, path):
        self.path = Path(str(path)).absolute()
    
    def __repr__(self):
        return str(self.path)

    def __str__(self):
        return str(self.path)

    def myls(self):
        files = []
        if self.path.is_dir():
            files = [ Mypath(x) for x in self.path.iterdir() ]
        else:
            files = [ Mypath(x) for x in self.path.parent.iterdir() ]
        return files

    def sizeofpath(self):
        if self.path.is_file() :
            print(str(self.path), " : ", self.path.stat().st_size)
            return self.path.stat().st_size
        elif  self.path.is_dir() :
            return sum([ x.sizeofpath() for x in self.myls()])

if __name__ == "__main__":
    mp = Mypath(".")
    print(mp.myls())
    print(mp.sizeofpath())
