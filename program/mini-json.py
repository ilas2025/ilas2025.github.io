
import pandas as pd
import json

minis = pd.read_csv("minis.csv").set_index("SID")
mini_speakers = pd.read_csv("mini-speakers.csv")
mini_all = minis.copy()

sdata = []
for SID in minis.index:
    mask = (mini_speakers.TYPE == SID)
    query = mini_speakers.loc[mask, ["NAME", "TITLE"]].to_json(orient="records")
    sdata.append(json.loads(query))

mini_all["SPEAKERS"] = sdata
mini_all.reset_index(inplace=True)
mini_all_json = mini_all.to_json(orient="records")
mini_all_json = json.dumps(json.loads(mini_all_json), indent=4)
with open("mini-all.json", "w") as f:
    f.write(mini_all_json)
