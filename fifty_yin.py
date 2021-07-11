# %%
import pandas as pd

fifty_soft = pd.read_csv('fifty_soft.csv', sep='\t', header=0)
fifty_hard = pd.read_csv('fifty_hard.csv', sep='\t', header=0)

# %%

fifty_hard = fifty_hard.reset_index().rename(
    columns={'index': 'initial'})
fifty_hard['type'] = 'hard'
fifty_soft = fifty_soft.reset_index().rename(
    columns={'index': 'initial'})
fifty_soft['type'] = 'soft'
fifty_df = pd.concat([fifty_hard, fifty_soft], axis=0)
fifty_df
# %%
