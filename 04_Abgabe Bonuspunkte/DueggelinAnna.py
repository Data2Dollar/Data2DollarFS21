import twint

c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"
c.Output = "DueggelinAnna.json"


twint.run.Search(c)



