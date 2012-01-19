BaseModel = require("models/models").BaseModel

# Describes an application installed in mycloud.
class exports.InstalledApp extends BaseModel

  url: '/api/installed-apps/'

  constructor: (app) ->
    super()
    @slug = app.slug
    @name = app.name
    @path = "/#{app.slug}/"
    
