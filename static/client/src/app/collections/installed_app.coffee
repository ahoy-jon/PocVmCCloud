App = require("models/installed_app").InstalledApp

class exports.InstalledAppCollection extends Backbone.Collection

  model: App
  url: '/api/installed-apps/'

  constructor: () ->
    super()

  # Select which field from backend response to use for parsing to populate
  # collection.
  parse: (response) ->
    response.rows

