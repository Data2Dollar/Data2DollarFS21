import twint

#Configuration
c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"
c.Store_json = True
c.Output = "HaeusermannDaniel.json"

#Running
twint.run.Search(c)
