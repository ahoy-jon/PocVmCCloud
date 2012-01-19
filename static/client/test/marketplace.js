
  describe('Navigation', function() {
    it('When I display home page', function() {
      return $("#home-button").click();
    });
    it('should displays 0 app installed', function() {
      return expect($("app").length).to.be(0);
    });
    it('When I display marketplace page', function() {
      return $("#market-button").click();
    });
    return it('should displays 2 apps available', function() {
      return expect($(".available-app").length).to.be(0);
    });
  });

  describe('Installation', function() {
    describe('When I click on hello 01 installation', function() {
      return it('should displayed a message to tell me that installation is done', function() {
        return expect(false).to.be.ok();
      });
    });
    describe('When I display home page', function() {
      it('should displays 1 app installed', function() {
        return expect(false).to.be.ok();
      });
      return it('should displays a link to the application', function() {
        return expect(false).to.be.ok();
      });
    });
    return describe('When I display marketplace page', function() {
      it('should displays 1 apps available', function() {
        return expect(false).to.be.ok();
      });
      return it('should displays first app as installed', function() {
        return expect(false).to.be.ok();
      });
    });
  });

  describe('Uninstallation', function() {
    describe('When I display home page', function() {
      return it('should displays 1 app installed', function() {
        return expect(false).to.be.ok();
      });
    });
    describe('When I click on first app remove button', function() {
      return it('a message is displayed to tell me that removal is done', function() {
        return expect(false).to.be.ok();
      });
    });
    describe('When I display marketplace page', function() {
      return it('should displays 2 apps available', function() {
        return expect(false).to.be.ok();
      });
    });
    return describe('When I display home page', function() {
      return it('should displays 0 app installed', function() {
        return expect(false).to.be.ok();
      });
    });
  });
