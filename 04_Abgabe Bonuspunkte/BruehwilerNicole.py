import twint

c = twint.Config()

c.Username = "ABack"
c.Since = "2010-01-01"
c.Until = "2021-03-12"
c.Store_json = True
c.Output = "BruehwilerNicole.JSON"

twint.run.Search(c)