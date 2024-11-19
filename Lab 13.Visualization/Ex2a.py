import json
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json('')

df = pd
df['tips'] = pd.tp_numeric(df['tips'])

tips_by_payment = df.groupby('payment_type')['tips'].sum()

plt.bar(list(tips_by_payment.index), tips_by_payment.tolist())
plt.show()