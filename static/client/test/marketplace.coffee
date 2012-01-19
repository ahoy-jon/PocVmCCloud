describe 'Navigation', ->

    it 'When I display home page', ->
      $("#home-button").click()

    it 'should displays 0 app installed', ->
      expect($("app").length).to.be(0)

    it 'When I display marketplace page', ->
      $("#market-button").trigger("click")

    it 'should displays 2 apps available',  ->
      expect($(".available-app").length).to.be(2)


describe 'Installation',  ->

  describe 'When I click on hello 01 installation', ->
    it 'should displayed a message to tell me that installation is done', () ->
      expect(false).to.be.ok()

  describe 'When I display home page', ->
    it 'should displays 1 app installed', () ->
      expect($("app").length).to.be(0)

    it 'should displays a link to the application', () ->
      expect(false).to.be.ok()

  describe 'When I display marketplace page', ->
    it 'should displays 1 apps available', () ->
      expect(false).to.be.ok()
    it 'should displays first app as installed', () ->
      expect(false).to.be.ok()


describe 'Uninstallation',  ->

  describe 'When I display home page', ->
    it 'should displays 1 app installed', () ->
      expect(false).to.be.ok()
      
  describe 'When I click on first app remove button', ->
    it 'a message is displayed to tell me that removal is done', () ->
      expect(false).to.be.ok()

  describe 'When I display marketplace page', ->
    it 'should displays 2 apps available', () ->
      expect(false).to.be.ok()

  describe 'When I display home page', ->
    it 'should displays 0 app installed', () ->
      expect(false).to.be.ok()

