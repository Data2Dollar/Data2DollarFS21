import twint

# Configure
c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"
c.Until = "2021-03-10"
c.Store_json = True
c.Output = "KayserTimon.json"

# Running search
twint.run.Search(c)


