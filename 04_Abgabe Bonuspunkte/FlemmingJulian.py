import twint

c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"
c.Store_json = True
c.Output = "FlemmingJulian.json"

twint.run.Search(c)