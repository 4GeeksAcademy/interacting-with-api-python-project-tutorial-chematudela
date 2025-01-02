import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib

# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

#accedemos a los datos por medio de las credenciales que hemos obtenido

acceso = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id,
client_secret = client_secret))

# Voy a trabajar sobre el grupo "Mumford and Sons"

MUMSONS_ID = "3gd8FJtBJtkRxdfbTu19U2"

#cramos una variable con los datos de las mejores canciones 

mejores_canciones = acceso.artist_top_tracks(MUMSONS_ID)

# de toda la info del diccionario, nos limitamos al campo traks

tracks = mejores_canciones["tracks"]

# imprimismos el top 10 por pantalla. 

for idx, track in enumerate(tracks):
    print(f"{idx + 1}. {track['name']} (Popularidad: {track['popularity']}) (Duración : {round(track['duration_ms']/1000/60,2)} minutos)")

#quitamos ruido y volcamos en una nueva variable


tracks_filtrada = [{"name": track["name"], "popularity": track["popularity"], "time":round(track['duration_ms']/1000/60,2)} for track in tracks]

#generamois el dataframe apartir de la variable filtrada y lo ordenamos de mayor a menor

tracks_dataframe = pd.DataFrame.from_records(tracks_filtrada)
tracks_dataframe.sort_values(["popularity"],ascending = False, inplace = True)

print(tracks_dataframe.head(3))

#genermos un fráfico simple de dispersión y lo volcamos a un png

grafico_disper = sns.scatterplot(data = tracks_dataframe, x = "popularity", y = "time")

fig = grafico_disper.get_figure()
fig.savefig("grafico_disper.png")

#con la info del gráfico, parece que las variables popularity y time NO están relacionadas entre ellas. 



