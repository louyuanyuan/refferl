df_18=df.ix[df['year']==2018]
df_ts=df_18[['n_killed','date']]
df_ts.index=df_18['date']
df_ts['n_killed'].plot(figsize=(15,6), color="green")
plt.xlabel('Year')
plt.ylabel('No. of Deaths')
plt.title("Death due to Gun Violence Time-Series Visualization")
plt.show()


from fbprophet import Prophet
sns.set(font_scale=1) 
df_date_index = df_18[['date','n_killed']]
df_date_index = df_date_index.set_index('date')
df_prophet = df_date_index.copy()
df_prophet.reset_index(drop=False,inplace=True)
df_prophet.columns = ['ds','y']

m = Prophet()
m.fit(df_prophet)
future = m.make_future_dataframe(periods=365,freq='D')
forecast = m.predict(future)
fig = m.plot(forecast)
plt.show()

m.plot_components(forecast);
plt.show()