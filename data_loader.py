import pandas as pd

def LoadDataFromGithub(lang, filename):
    '''
    lang - en or cn
    filename - Orchestrion, OrchetrionCategory, OrchestrionPath
    '''
    if lang == cn:
        url = 'https://raw.githubusercontent.com/thewakingsands/ffxiv-datamining-cn/'
    else:
        url = 'https://raw.githubusercontent.com/xivapi/ffxiv-datamining/tree/master/csv/'
    return pd.read_csv(url+filename+'.csv', header = None)
