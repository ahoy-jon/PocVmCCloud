class exports.InstalledApp extends Backbone.Model

  url: '/api/installed-apps/'

  constructor: (app) ->
    super()
    @slug = app.slug
    @name = app.name
    @path = "/#{app.slug}/"
    
  isNew: () ->
    @id is undefined
