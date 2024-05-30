import csv, json
import langdetect

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
            
# seed_tracks = []
# with open("songs.jsonl") as f:
#     for d in f:
#         data = json.loads(d)
#         seed_tracks.append(data["id"]+" "+data["name"]+"\n")

# with open("seed-tracks2", "w") as f:
#     f.writelines(seed_tracks)

# from transformers import pipeline

# model_ckpt = "papluca/xlm-roberta-base-language-detection"
# pipe = pipeline("text-classification", model=model_ckpt)

# freq = {}
# with open("seed-tracks2") as f:
#     names = [l.split()[0] for l in f]
#     langs = pipe(names)
#     langs = [lang["label"] for lang in langs]
#     freq = {lang:langs.count(lang) for lang in set(langs)}

# for k,v in freq.items():
#     print(k,":",v)

    
# with open("songs.csv") as f:
#     reader = csv.reader(f)
#     song_count, artist_count, max_artists = 0,0,0
#     for r in reader:
#         song_count += 1
#         artists = len(r[1].split())
#         artist_count += artists
#         max_artists = artists if artists > max_artists else max_artists
#     print(artist_count/song_count, max_artists, song_count)

# songs = []
# with open("songs.jsonl") as f:
#     for l in f:
#         data = json.loads(l)
#         name = data["name"] + " | " + ", ".join([artist["name"] for artist in data["artists"]])
#         songs.append(name)

# with open("song-names", "w") as f:
#     f.write("\n".join(songs))

import os
with open("song-names2") as f:
    for s in f:
        os.system(f"yt-dlp -x -q -S +size --download-archive ./music/songlist --max-filesize \"10M\" -o \"./music/%(title)s.%(ext)s\" \"ytsearch:{s}\"")
