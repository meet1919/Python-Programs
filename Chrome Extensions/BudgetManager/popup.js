$(function(){

chrome.storage.sync.get(['total', 'limit'], function(budget){
    $('#total').text(budget.total);
    $('#limit').text(budget.limit);
})

    $('#spendAmount').click(function(){
        chrome.storage.sync.get(['total', 'limit'], function(budget){
            var newTotal = 0;
            if (budget.total){
                newTotal += parseInt(budget.total);
            }

            var amount = $('#amount').val();
            if(amount){
                newTotal += parseInt(amount);
            }

            chrome.storage.sync.set({'total': newTotal}, function(){   // Setting 'total' value in chrome storage to newTotal
                if (amount && newTotal >= budget.limit){
                    var notifOptions = {
                        type: "basic", 
                        iconUrl: "icon48.png",
                        title: "Limit reached!",
                        message: "Uh oh! looks like you reached your limit"
                    };
                    chrome.notifications.create('limitNotif', notifOptions);
                }
                
            }); 

            $('#total').text(parseInt(newTotal));
            $('#amount').val('');  // Reseting input bar to empty

        });
    });
});