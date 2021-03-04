import twint

c = twint.Config()
c.Username = "ABack"
c.Output = "aback.csv"

twint.run.Search(c)



