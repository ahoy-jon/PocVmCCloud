BaseCollection = require("collections/collections").BaseCollection
App = require("models/installed_app").InstalledApp


# List of installed applications.
class exports.InstalledAppCollection extends BaseCollection
    
  model: App
  url: '/api/installed-apps/'

  constructor: () ->
    super()


