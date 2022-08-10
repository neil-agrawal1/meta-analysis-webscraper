import pandas as pd 

pd.set_option("display.max_rows", 400, "display.max_columns", 2)
pubmeddois_df = pd.read_csv('pubmed/pubmeddois.csv', encoding='latin')
crossrefdois_df = pd.read_csv('crossref/crossrefdois.csv', encoding='latin')
scholardois_df = pd.read_csv('scholar/scholarseleniuminfo.csv', encoding='latin')

pubmeddoisclean_df = pubmeddois_df[~pubmeddois_df['DOI'].str.contains("No DOI")]
scholardois_df = scholardois_df.dropna(axis=0)
crossrefdois_df[crossrefdois_df.duplicated() == True]

del scholardois_df['Abstract']
print(scholardois_df)

alldois = pd.concat([pubmeddoisclean_df, crossrefdois_df, scholardois_df], axis=0, ignore_index=True, verify_integrity=True).drop_duplicates()
print(alldois)
alldois.to_csv('dois.csv', index=None)
