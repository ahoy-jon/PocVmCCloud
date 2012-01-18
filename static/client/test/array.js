
  describe('Array', function() {
    return describe('#indexOf()', function() {
      return it('should return -1 when the value is not present', function() {
        expect([1, 2, 3].indexOf(4)).to.be(-1);
        return expect([1, 2, 3].indexOf(2)).to.be(3);
      });
    });
  });
