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
          console.log(results.content); //results.data should be a JSON object

            Chart.defaults.global.responsive = true;
            Chart.defaults.global.animation = false;
            $(function(){
            var data = [
              {
                label: 'Bubble chart example',
                strokeColor: 'rgba(77, 180, 73, 0.3)',
                data: [
                  { x: 1, y: 10, r: 7 }, { x: 2, y: 12, r: 5 }, { x: 3, y: 14, r: 10 }, { x: 4, y: 18, r: 6 },
                  { x: 5, y: 26, r: 9 }, { x: 6, y: 42, r: 4 }, { x: 7, y: 60, r: 8 }
                ]
              }
            ];

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