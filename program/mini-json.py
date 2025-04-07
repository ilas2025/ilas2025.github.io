
import pandas as pd
import json

minis = pd.read_csv("minis.csv").set_index("MID")
mini_speakers = pd.read_csv("mini-speakers.csv")
mini_all = minis.copy()

sdata = []
for mid in minis.index:
    mask = (mini_speakers.TYPE == mid)
    query = mini_speakers.loc[mask, ["NAME", "TITLE"]].to_json(orient="records", force_ascii=False)
    sdata.append(json.loads(query))

mini_all["SPEAKERS"] = sdata
# mini_all.reset_index(inplace=True)
mini_all_json = mini_all.to_json(orient="index", force_ascii=False, indent=4)
with open("mini-all.json", "w", encoding='utf-8') as f:
    f.write(mini_all_json)
