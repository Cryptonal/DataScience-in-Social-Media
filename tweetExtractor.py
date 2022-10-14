import twint
import nest_asyncio
import pandas as pd

nest_asyncio.apply()
c = twint.Config()

c.Username = "julian_bereza"
#["Lockdown", "Curfew", "Corona", "Safe Distance", "Covid-19"]
c.Search = ['querdenken']
c.Lang = "en"
c.limit = 100
#c.Since = "2020–11–01 00:00:00"
#c.Until = "2021–05–31 00:00:00"
c.Store_csv = True
c.Output = "Julian_Bereza"
#c.Pandas = True

# Run
twint.run.Search(c)

def columne_names():
    return twint.output.panda.Tweets_df.columns

def twint_to_pd(columns):
    return twint.output.panda.Tweets_df[columns]