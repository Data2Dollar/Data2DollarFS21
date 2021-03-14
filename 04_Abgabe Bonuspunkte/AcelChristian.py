import twint

c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"
c.Store_json = True
c.Output = "AcelChristian.json"

twint.run.Search(c)

# Trotz längerer Recherche und verschiedenster Versuche erscheint immer Folgendes:
# ModuleNotFoundError: No module named 'twint'
# Ich schreibe morge dazu einen Betrag ins Diskussionforum.
