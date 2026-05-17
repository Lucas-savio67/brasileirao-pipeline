import requests
import pandas as pd

TOKEN = "59cc6011c1214ec9924994a6ba88d1cf"  # coloca seu token aqui

def buscar_partidas(temporada: int = 2024) -> pd.DataFrame:
    url = "https://api.football-data.org/v4/competitions/BSA/matches"
    headers = {"X-Auth-Token": 	TOKEN}
    params = {"season": temporada}

    response = requests.get(url, headers=headers, params=params)
    dados = response.json()

    partidas = dados["matches"]
    
    df = pd.DataFrame([{
        "data": p["utcDate"],
        "casa": p["homeTeam"]["name"],
        "fora": p["awayTeam"]["name"],
        "gols_casa": p["score"]["fullTime"]["home"],
        "gols_fora": p["score"]["fullTime"]["away"],
        "status": p["status"]
    } for p in partidas])

    return df

if __name__ == "__main__":
    df = buscar_partidas()
    print(df.head(10))
    print(f"\nTotal de partidas: {len(df)}")
    df.to_csv("../data/partidas.csv", index=False)
    print("Arquivo salvo em data/partidas.csv")