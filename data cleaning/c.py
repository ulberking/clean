import pandas as pd
df = pd.read_csv('fianldata.csv')
print(df.shape)
del df['sy_gaiamagerr2']
del df['sy_gaiamagerr1']
del df['st_tefferr1']
del df['st_tefferr2']
del df['st_tefflim']
del df['st_rad']
del df['st_raderr1']
del df['st_raderr2']
del df['st_radlim']
del df['st_mass']
del df['st_masserr1']
del df['st_masserr2']
del df['st_masslim']
del df['st_met']
del df['st_meterr1']
del df['st_meterr2']
del df['st_metlim']
del df['st_metratio']
del df['st_logg']
del df['st_loggerr1']
del df['st_loggerr2']
del df['st_logglim']
del df['rastr']
del df['ra']
del df['decstr']
del df['dec']
del df['sy_dist']
del df['sy_disterr1']
del df['sy_disterr2']
del df['sy_vmag']
del df['sy_vmagerr1']
del df['sy_vmagerr2']
del df['sy_kmag']
del df['sy_kmagerr1']
del df['sy_kmagerr2']
del df['sy_gaiamag']
print(df.shape)
df.to_csv('clean.csv')
df1 = pd.read_csv('clean.csv')
print(df1.shape)