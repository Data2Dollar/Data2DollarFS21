import twint

c = twint.Config()
c.Username = "ABack"
c.Store_json = True
c.Output = "ScholtysikMadleina.json"
c.Since = '2010-01-01'
c.Until = '2021-03-14'

twint.run.Search(c)
