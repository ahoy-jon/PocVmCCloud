homeTemplate = require('../templates/home')

AppRow = require('views/installed_app').InstalledAppRow
AppCollection = require('collections/installed_app').InstalledAppCollection


class exports.HomeView extends Backbone.View
  id: 'home-view'


  ### Constructor ###

  constructor: ->
    super()

    @apps = new AppCollection()
    @apps.bind('reset', @fillApps)

 
  ### Listeners ###

  ### Functions ###

  # Load data from server
  fetchData: ->
    @apps.fetch()

  # Grabs categories from server then display them as a list.
  fillApps: =>
    @appList = $("#app-list")
    @appList.html null
    @apps.forEach (app) =>
      row = new AppRow app
      el = row.render()
      @appList.append el
 

  render: ->
    $(@el).html homeTemplate()
    @appList = $("#app-list")

    @el

