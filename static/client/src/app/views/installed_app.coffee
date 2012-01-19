template = require('../templates/installed_app')
BaseRow = require('views/row').BaseRow

class exports.InstalledAppRow extends BaseRow

  className: "installed-app"

  events:
    "click .button": "onRemoveClicked"

  constructor: (@model) ->
    super(@model)

  # Events 

  onRemoveClicked: (event) =>
    event.preventDefault()
    @removeApp()

  # Functions

  removeApp: ->
    @$(".info-text").html "Removing..."
    $.ajax
     type: 'DELETE'
     url: "/api/installed-apps/#{@id}/"
     success: =>
       @$(".info-text").html "Removed!"
     error: =>
       @$(".info-text").html "Remove failed."

  render: ->
    $(@el).html(template(app: @model))
    @el

