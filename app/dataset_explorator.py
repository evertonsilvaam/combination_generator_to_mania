import pandas as pd

def read_dataframe():
    dataframe = pd.read_excel("resultados.xlsx")
    #print(dataframe.head())
    return dataframe

dataframe = read_dataframe()

args = {
    "max" : 107,
    "min" : 68
}

#print(dataframe.head())

def more_frequence(dataframe):
    #size = len(dataframe)
    good_numbers = []
    bad_numbers = []
    best_numbers = []
    worse_numbers = []
    #print(size)
    #print(dataframe.iloc[[0]]["bola 15"])
    #for linha in range(size):
    #    print(linha)
    #    print(dataframe.iloc[[linha]])
    #print(dataframe["bola 1"].value_counts())
    colunas_validas = dataframe.columns[2:]
    #colunas_validas = ["bola 1", "bola 2", "bola 3", "bola 4", "bola 5", "bola 6", "bola 7", "bola 8"]
    #print(colunas_validas)
    for coluna in colunas_validas:
        valores = dataframe[coluna].value_counts()
        #print(valores)
        #print("num",valores.index)
        #print("qtde",valores.values)
        index = 0
        for i in valores:
            if (i >= args["max"]):
                good_numbers.append(valores.index[index])
            elif (i <= args["min"]) :
                bad_numbers.append(valores.index[index])
            #print(i)
            index +=1

            #if (index == 1): break
        #print(valores.values)
        good_numbers = list(set(good_numbers))
        good_numbers.sort()

        bad_numbers = list(set(bad_numbers))
        bad_numbers.sort()
    print("Good Numbers:", good_numbers)
    #print("Good Numbers:", len(good_numbers))
    print("Bad Numbers:", bad_numbers)
    for i in bad_numbers:
        if i in good_numbers:
            good_numbers.remove(i)
            best_numbers.append(i)
        else:
            worse_numbers.append(i)
            
    print("Good Numbers:", good_numbers)
    print("Best Numbers:", best_numbers)
    print("Worse Numbers:", worse_numbers)
    #teste = good_numbers.remove(i for i in bad_numbers)

    #print("real:", good_numbers - bad_numbers)
        #for i in valores:
        #    if (valores.value>100):
        #        print(valores.index)

    """
    01	02	05	07	08
    10	11	13	14	15
    16	18	21	22	24

    """

more_frequence(dataframe)

def include_competition(dataframe, index, date, numbers, label):
    print(dataframe)


def include_win_cols(dataframe):
    dataframe['label'] = 1
    print(dataframe.head())

#include_win_cols(dataframe)

#include_competition(dataframe, 2261, "03/07/2021", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 0)
