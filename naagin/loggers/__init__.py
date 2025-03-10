from logging import getLogger

app = getLogger("naagin")

api = app.getChild("api")
api01 = app.getChild("api01")
game = app.getChild("game")

setting = app.getChild("setting")
model = app.getChild("model")
schema = app.getChild("schema")
