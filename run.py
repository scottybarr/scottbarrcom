from blog import app, config
app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
