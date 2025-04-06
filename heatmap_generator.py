import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime
from matplotlib.dates import DateFormatter

# 1. Récupération des données
def get_data():
    url = "https://api.thingspeak.com/channels/2907557/feeds.json?api_key=5D8MDD8F22GW1K6L&results=100"
    data = requests.get(url).json()['feeds']
    df = pd.DataFrame(data)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['field1'] = pd.to_numeric(df['field1'])  # Température
    df['field2'] = pd.to_numeric(df['field2'])  # pH
    return df

# 2. Génération du heatmap
def generate_heatmap(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['created_at'], df['field1'], c=df['field2'], cmap='RdYlGn_r', s=100)
    plt.colorbar(label='pH')
    plt.title(f"Heatmap Température/pH\n{datetime.now().strftime('%Y-%m-%d %H:%M')}")
    plt.xlabel('Date')
    plt.ylabel('Température (°C)')
    plt.gca().xaxis.set_major_formatter(DateFormatter('%m/%d %H:%M'))
    plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()

# 3. Exécution
df = get_data()
if not df.empty:
    generate_heatmap(df)
    print("Heatmap généré avec succès !")
else:
    print("Aucune donnée disponible")