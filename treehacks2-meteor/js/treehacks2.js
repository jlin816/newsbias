if (Meteor.isServer) {
    Meteor.methods({
        checkSentiment: function (searchTerm) {
            this.unblock();
            return Meteor.http.call("GET", "https://agile-escarpment-65178.herokuapp.com/newsbiasapp/getData?q=" + searchTerm);
        }
    });
}

if (Meteor.isClient) {
  // This code only runs on the client

  Template.search.events({
        'submit form' : function (event) {
          event.preventDefault();
          var searchTerm = event.target.search.value;
          console.log(searchTerm);
          Meteor.call("checkSentiment", searchTerm, function(error, results) {
          //console.log(results.content); //results.data should be a JSON object
          });
        }
    });
}