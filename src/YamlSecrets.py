import os

class YamlSecrets:
    def __init__(self, path, absolute=True):
        if absolute:
            self.absoluteFilePath = path
        else:
            workingFolder = os.path.dirname(os.path.abspath(__file__))
            relativeFilePath = path
            self.absoluteFilePath = os.path.join(workingFolder, relativeFilePath)

        print("[yaml secrets] path:", self.absoluteFilePath)
        self.dictionary = {}
        self.load()
        print("[yaml secrets] loaded:", self.dictionary)


    def load(self):
        self.dictionary = {}
        f = open(self.absoluteFilePath, "r")
        raw = f.read()
        f.close()
        lines = raw.split('\n')
        for l in lines:
            if l:
                split = l.split(":", 1)
                key = split[0].strip()
                val = split[1].strip()
                self.dictionary[key] = val


    def find(self, key):
        try:
            return self.dictionary[key]
        except:
            return None
