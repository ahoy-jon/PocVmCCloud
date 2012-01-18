window.app = {}
app.routers = {}
app.models = {}
app.collections = {}
app.views = {}

MainRouter = require('routers/main_router').MainRouter
HomeView = require('views/home_view').HomeView

# app bootstrapping on document ready
$(document).ready ->
  app.initialize = ->
    app.routers.main = new MainRouter()
    app.views.home = new HomeView()

    if Backbone.history.getFragment() is ''
      app.routers.main.navigate 'home', true
    else
      app.routers.main.navigate Backbone.history.getFragment(), true

      
  app.initialize()
  Backbone.history.start()
