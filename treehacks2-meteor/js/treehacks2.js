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

  Template.search.jsonparser = function(){
    return JSON.parse(this.MESSAGE);
  };

  Template.search.events({
        'submit form' : function (event) {
          event.preventDefault();
          var searchTerm = event.target.search.value;
          console.log(searchTerm);
          Meteor.call("checkSentiment", searchTerm, function(error, results) {

            Chart.defaults.global.responsive = true;
            Chart.defaults.global.animation = false;
            $(function(){
            var data = [
              {
                label: 'Perspective',
                strokeColor: 'rgba(77, 180, 73, 0.3)',
                data: []
              }
            ];

            var i = 2;
            var arr = $.parseJSON(results.content);
            $(arr).each(function() {
              data[0].data.push({x: this.bucket, y: 2, r: 2})
              i = i + 1;
            });

            var ctx = document.getElementById("myBubbleChart").getContext("2d");
            var myBubbleChart = new Chart(ctx).Scatter(data, {
              bezierCurve: true,
              showTooltips: true,
              scaleShowHorizontalLines: true,
              scaleShowLabels: true,
              scaleBeginAtZero: true,
              datasetStroke: false
              });
            });


          });
        }
    });
}