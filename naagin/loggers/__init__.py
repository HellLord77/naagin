from logging import getLogger

app = getLogger("naagin")

api = app.getChild("api")
api01 = app.getChild("api01")
game = app.getChild("game")
cdn01 = app.getChild("cdn01")
www = app.getChild("www")

setting = app.getChild("setting")
model = app.getChild("model")
route = app.getChild("route")
schema = app.getChild("schema")
