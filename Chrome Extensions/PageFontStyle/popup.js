$(function(){
    
    var color = $("#fontColor").val();
    $('#fontColor').on("change paste keyup", function(){
        color = $(this).val();
    });

    $('#btnChange').click(function(){
        var element = String($('#classType').val());
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
            chrome.tabs.sendMessage(tabs[0].id, {todo: "changeColor", clickedColor: color, clickedElement: element})
        });
    });

    $('#btnBold').click(function(){
        var element = String($('#classType').val());
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
            chrome.tabs.sendMessage(tabs[0].id, {todo: "changeStyle", clickedElement: element})
        });
    });
});