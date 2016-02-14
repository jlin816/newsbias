document.addEventListener('DOMContentLoaded', function() {
  var checkPageButton = document.getElementById('checkPage');


    chrome.tabs.getSelected(null, function(tab) {
      d = document;
      console.log(tab)
      var siteUrl = encodeURIComponent(tab.url)
      var url ='https://access.alchemyapi.com/calls/url/URLGetTextSentiment?url='+siteUrl+'&apikey=e1b9fd7b092af9c2a292178a472898abcf3421e0&outputMode=json&jsonp=?';
      // var f = d.createElement('form');
      // f.action =url;
      // f.method ='post';
      // console.log(data);
      // f.submit();
      $.getJSON(url,function(data){
            console.log(data);
            $('#junk').html(data.docSentiment.score)  
               });


    
      //$.getJSON( "ajax/test.json", function( data ) {
      //var items = [];
      //$.each( data, function( key, val ) {
      //items.push( "<li id='" + key + "'>" + val + "</li>" );
      //  });
 
      //$( "<ul/>", {
      //"class": "my-new-list",
      //html: items.join( "" )
      //}).appendTo( "body" );

      //});

    
      //f.action = 'http://gtmetrix.com/analyze.html?bm';
      //f.method = 'post';
      //var i = d.createElement('input');
      //i.type = 'hidden';
      //i.name = 'url';
      //i.value = tab.url;
      //f.appendChild(i);
      //d.body.appendChild(f);
      //f.submit();
    });

}, false);