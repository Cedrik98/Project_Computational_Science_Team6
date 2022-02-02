# Program create plots for data from our Netlogo model. Netlogo creates .csv
# using the behaviour space tool. Experiments are included in the Netlogo file.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame()
print(df)

# i loops over vacination percentage. j loops over total crowd size. The
# way we set up the results allows us to create a dataframe this way. We
# then plot the result using seaborn.
for i in [0, 70.6, 100]:
    for j in [2000, 2500, 3333, 5000, 10000]:
        df_temp = pd.read_csv('Model_output/Model_final-version ' +
                              str(j) + '_people_' + str(i) +
                              'pct_vacinated-spreadsheet.csv',
                              skiprows=168, header=None)
        df_temp = df_temp.T
        df_temp.columns = ['R']
        df_temp['vaccination'] = pd.Series([i for x in
                                            range(len(df_temp.index))])
        df_temp['population size'] = pd.Series([j for x in
                                                range(len(df_temp.index))])
        df = pd.concat([df, df_temp[1::]], ignore_index=True)
print(df)

sns.lineplot(x="population size", y="R", hue='vaccination', data=df)
plt.show()
