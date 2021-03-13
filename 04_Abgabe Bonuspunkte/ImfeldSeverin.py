import twint

# Configuration
s = twint.Config()
s.Username = "ABack"
s.Since = "2010-01-01"
s.Until = "2021-03-13"
s.Store_json = True
s.Output = "ImfeldSeverin.json"

# Run Search
twint.run.Search(s)