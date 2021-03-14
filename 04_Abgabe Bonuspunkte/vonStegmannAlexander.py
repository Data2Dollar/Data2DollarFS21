import twint
import json

c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01 00:00:00"
c.Store_json = True
c.Output = "ABack_raw.json"
twint.run.Search(c)

# https://stackoverflow.com/questions/51919698/cant-parse-json-file-json-decoder-jsondecodeerror-extra-data
with open('ABack_raw.json') as f:
    data = json.loads("[" + f.read().replace("}\n{", "},\n{") + "]")

with open('ABack_tweets.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
