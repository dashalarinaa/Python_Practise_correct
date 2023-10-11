import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


# с помощью этой функции приводим к one hot encoding, запускала в google colaboratory
pd.get_dummies(data['whoAmI'], drop_first = True)