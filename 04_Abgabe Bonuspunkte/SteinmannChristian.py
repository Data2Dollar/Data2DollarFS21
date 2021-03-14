import twint
import json

c = twint.Config()

c.Username = "ABack"
c.Store_json = True
c.Since = "2010-01-01 00:00:00"
c.Output = "ProfDrABack.json"

twint.run.Search(c)
