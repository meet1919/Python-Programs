   chrome.runtime.sendMessage({todo: "showPageAction"}); 

   chrome.runtime.onMessage.addListener(function(request, sender, sendResponse){
       if (request.todo == "changeColor") {
           var addColor = '#' + request.clickedColor
           $(request.clickedElement).css('color', addColor);
       }
       if (request.todo == "changeStyle") {
           $(request.clickedElement).css('font-weight', "bold");
       }
   });