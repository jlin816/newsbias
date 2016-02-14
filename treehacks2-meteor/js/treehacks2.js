if (Meteor.isServer) {
    Meteor.methods({
        checkSentiment: function () {
            this.unblock();
            return Meteor.http.call("GET", "http://search.twitter.com/search.json?q=happytweets");
        }
    });
}

if (Meteor.isClient) {
  // This code only runs on the client

  Template.search.events({
        'click #search-sentiment' : function () {
          event.preventDefault();
          Meteor.call("checkSentiment", function(error, results) {
          console.log("Hello"); //results.data should be a JSON object
          });
        }
    });
}