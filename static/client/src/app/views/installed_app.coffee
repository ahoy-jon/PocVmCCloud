appTemplate = require('../templates/installed_app')

class exports.InstalledAppRow extends Backbone.View

  tagName: "div"
  className: "installed-app"

  constructor: (@model) ->
    super()
    
    @id = @model.slug
    @model.view = @

  remove: ->
    $(@el).remove()

  render: ->
    $(@el).html(appTemplate(app: @model))
    @el

