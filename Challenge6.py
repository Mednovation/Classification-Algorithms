import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


if __name__ == '__main__':
    
    df = pd.read_excel('test.xlsx', sheetname='Sheet1')
    
    f = open("metadata.txt", "w+")
    
    for i in df.index:
        for j in df.columns:
            cell = str(df[j][i])
            if cell == '':
                f.write(j + ": " + 'NaN' + "\n")
            else:
                f.write(j + ": " + cell + "\n")
        f.write("\n" + "~~~" + "\n")
    f.close()
