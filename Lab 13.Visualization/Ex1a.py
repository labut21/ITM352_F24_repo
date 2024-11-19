import json
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json('https://drive.google.com/file/d/1-kvj2Ore88PGzZ9J7_lPBOvNf5C1ohpQ')

x = df(['trip_miles'])
plt.hist(x)
plt.show()