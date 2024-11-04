import gdown # use gdown because in data have large file

direct_link = {'lectures': 'https://drive.google.com/uc?export=download&id=1QMsR174yRaA8CxRGFaOC2Fcm8B5Fv2Tr',
               'questions': 'https://drive.google.com/uc?export=download&id=11ab4rOtRCJdP2enuAOTccj8Ko9iT_b6r',
               'train': 'https://drive.google.com/uc?export=download&id=1qZr6g9mRtWdCj2Z6dw7nvnVov1XueSws'}

def get_data():
    for i in direct_link.keys():    
        url = direct_link[i]
        path = f'./data/{i}.csv'
        try:
            gdown.download(url, path)
            print (f'File {i}.csv download sucsessful!')
        except Exception as e:
            print(f'Download of {i}.csv is failed!')
            print(e)
