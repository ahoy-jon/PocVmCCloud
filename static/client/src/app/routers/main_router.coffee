class exports.MainRouter extends Backbone.Router
  routes :
    "home": "home"

  home: ->
    $('#content').html app.views.home.render()
    app.views.home.setListeners()
    app.views.home.apps.fetch()
