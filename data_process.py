import pandas as pd

#general port data
port_data = pd.read_excel('port_ship_data.xlsx')
#national ports
national_data = pd.read_excel('national_ports.xlsx',index_col=0)
#ocean freight container index data 
BDI = pd.read_excel('Baltic Dry Index.xlsx',index_col=0)

#select country for display
def select_country(df,countries):
    return df[countries]

#aggregated national port instance
nations = port_data['Country'].value_counts().to_frame().reset_index()

#aggregated port region instance
regions = port_data['Region'].value_counts().to_frame().reset_index()

#aggregated BDI cost index
freight_cost = BDI.T.mean().to_frame().reset_index().rename(columns={0:'Cost','index':'Year'})
