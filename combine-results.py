import os, glob 
import pandas as pd 


pd.set_option("display.max_rows", 400, "display.max_columns", 2)
pubmeddois_df = pd.read_csv('pubmed/pubmeddois.csv', encoding='latin')
crossrefdois_df = pd.read_csv('crossref/crossrefdois.csv', encoding='latin')

pubmeddoisclean_df = pubmeddois_df[~pubmeddois_df['DOI'].str.contains("No DOI")]
crossrefdois_df[crossrefdois_df.duplicated() == True]

# try:
#     alldois = pd.concat([pubmeddoisclean_df, crossrefdois_df], axis=0, ignore_index=True, verify_integrity=True)
# except ValueError as e: 
#     print('ValueError', e)
# print(alldois)

alldois = pd.concat([pubmeddoisclean_df, crossrefdois_df], axis=0, ignore_index=True, verify_integrity=True).drop_duplicates()
print(alldois)