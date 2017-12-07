var page = document.getElementById("button");


if(page){
  page.addEventListener("click", GetURL, false);
}


// chrome.runtime.onMessage.addListener(function(data){
//   if (data != undefined){
//     console.log(data.text);
//     upd(data.text);
//   }
// });

// function Get(){
//     chrome.tabs.create({'url': "http://www.supremenewyork.com/shop/all/pants"}, function(tabs){
//         var activeTab = tabs[0];
//         chrome.tabs.executeScript( {
//           file: 'back.js'
//         }, function() {
//         });
//         var activeTab = tabs[0];
//     });
// }

function GetURL(){
  chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
        var activeTab = tabs[0];
        chrome.tabs.executeScript( {
          file: 'back.js'
        }, function(result) {
        chrome.tabs.create({'url': result[0]});
        updt();
  });
});
};

function updt1(){
    chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
        var activeTab = tabs[0];
        chrome.tabs.executeScript( {
          code: "console.log('Hi');"
        }, function() {
            console.log(11);
        // chrome.tabs.create({'url': result[0]});
  });
});
}

// // function sleep(ms) {
// // ms += new Date().getTime(); while (new Date() < ms){}
// // chrome.tabs.create({'url': 'http://www.supremenewyork.com/shop/cart'});
// // } 

function updt(){
    chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
        var activeTab = tabs[0];
        chrome.tabs.executeScript( {
          code: "document.getElementsByName('commit')[0].click();"
        }, function() {
  });
  var ms = 1000; 
  ms += new Date().getTime(); 
  while (new Date() < ms){}
  chrome.tabs.create({'url': 'http://www.supremenewyork.com/shop/cart'});
  updt1();
});
}



