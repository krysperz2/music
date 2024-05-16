import requests, json, random

token = ""
token_auth_header = {"Content-Type": "application/x-www-form-urlencoded"}
token_auth_data = {"grant_type":"client_credentials", "client_id":"3dce90f0fee44ba98c7e9664950fb8bd","client_secret":"f88a8ed2610c44daa6218a8985d26640"}
try:
    with open("token-cache", "rw") as f:
        token = f.read()
        if token == "":
            res = requests.post("https://accounts.spotify.com/api/token", headers=token_auth_header, data=token_auth_data)
            token = json.loads(res.text)["access_token"]
            f.write(token)
except:
    res = requests.post("https://accounts.spotify.com/api/token", headers=token_auth_header, data=token_auth_data)
    token = json.loads(res.text)["access_token"]
    with open("token-cache", "w") as f:
        f.write(token)

auth_header = {"Authorization": f"Bearer {token}"}
api = "https://api.spotify.com/v1"
request_count = 0

seed_tracks = []
with open("seed-tracks") as f:
    seed_tracks = [i.split()[0] for i in f.read().split("\n")]

with open("songs-tmp.jsonl", "a") as f:
    while request_count < 1:
        request_count += 1
        recommendation_options = {"limit":100,
                                "seed_genres":"indian",
                                "min_popularity":50,
                                "seed_tracks":",".join(random.choices(seed_tracks,k=4))
                                # "target_popularity":90,
                                # "target_valence":random.random(),
                                # "target_danceability":random.random(),
                                # "target_energy":random.random(),
                                # "target_instrumentalness":random.random(),
                                # "target_liveness":random.random(),
                                # "target_loudness":random.random(),
                                # "target_speechiness":random.random()
                                }
        recommendation_options = "&".join([k+"="+str(v) for k,v in recommendation_options.items()])
        url = api+"/recommendations?"+recommendation_options
        res = requests.get(url, headers=auth_header)
        # print(res.text)
        tracks = json.loads(res.text)["tracks"]
        for t in tracks:
            f.write(json.dumps(t)+"\n")


# with open("genres.txt", "w") as f:
#     for genre in json.loads(requests.get(api+"/recommendations/available-genre-seeds", headers=auth_header).text)["genres"]:
#         f.write(genre+"\n")
