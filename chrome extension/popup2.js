document.addEventListener('DOMContentLoaded', function() {
  var checkPageButton = document.getElementById('checkPage');
  

    chrome.tabs.getSelected(null, function(tab) {
      d = document;

      var url ='http://access.alchemyapi.com/calls/url/URLGetTextSentiment?url=http%3A%2F%2Fwww.macrumors.com%2F2013%2F11%2F05%2Fapple-releases-itunes-11-1-3-with-equalizer-and-performance-improvements%2F&apikey=secret&outputMode=json&jsonp=?';
      f.action =url;
      f.method ='post';
      console.log(data);
      f.submit();
      $.getJSON(url,function(data){alert(data);});

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

      var f = d.createElement('form');
      f.action = 'http://gtmetrix.com/analyze.html?bm';
      f.method = 'post';
      var i = d.createElement('input');
      i.type = 'hidden';
      i.name = 'url';
      i.value = tab.url;
      f.appendChild(i);
      d.body.appendChild(f);
      f.submit();
    });
   
}, false);