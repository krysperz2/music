import csv, json

# with open("songs.jsonl") as f:
#     with open("songs.csv", "w") as f2:
#         writer = csv.writer(f2)
#         writer.writerow(["name", "artist_ids", "spotify_id", "album_name", "album_release_date"])
#         for s in f:
#             data = json.loads(s)
#             writer.writerow([data["name"],
#                              " ".join([a["id"] for a in data["artists"]]),
#                              data["id"],
#                              data["album"]["name"],
#                              data["album"]["release_date"]])
            
seed_tracks = []
with open("songs2.jsonl") as f:
    for d in f:
        data = json.loads(d)
        seed_tracks.append(data["id"]+" "+data["name"]+"\n")

with open("seed-tracks", "w") as f:
    f.writelines(seed_tracks)

# with open("songs.csv") as f:
#     reader = csv.reader(f)
#     song_count, artist_count, max_artists = 0,0,0
#     for r in reader:
#         song_count += 1
#         artists = len(r[1].split())
#         artist_count += artists
#         max_artists = artists if artists > max_artists else max_artists
#     print(artist_count/song_count, max_artists, song_count)