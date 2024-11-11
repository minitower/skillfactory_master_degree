import gdown # use gdown because in data have large file

def get_data():
    gdown.download('https://drive.google.com/uc?export=download&id=1Kb78mAWYKcYlellTGhIjPI-bCcKbGuTn', './data/data.csv')
