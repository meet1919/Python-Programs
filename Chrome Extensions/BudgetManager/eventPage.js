var menuItem = {
    "id": "spendMoney",
    "title": "Add Money",
    "contexts": ["selection"]
};

function isInt(value) {
    return !isNaN(value) && 
           parseInt(Number(value)) == value && 
           !isNaN(parseInt(value, 10));
}
chrome.contextMenus.create(menuItem);

chrome.contextMenus.onClicked.addListener(function(clickdata){
    if (clickdata.menuItemId == "spendMoney" && clickdata.selectionText){
        if (isInt(clickdata.selectionText)) {
            chrome.storage.sync.get(['total', 'limit'], function(budget){
                var newTotal = 0;
                if (budget.total){
                    newTotal += parseInt(budget.total);
                }
                newTotal += parseInt(clickdata.selectionText);
                chrome.storage.sync.set({'total': newTotal}, function(){
                    if (newTotal >= budget.limit){
                        var notifOptions = {
                            type: "basic", 
                            iconUrl: "icon48.png",
                            title: "Limit reached!",
                            message: "Uh oh! looks like you reached your limit"
                        };
                        chrome.notifications.create('limitNotif', notifOptions);
                    }
                });
            });
        }
    }
});
chrome.storage.onChanged.addListener(function(changes, storageName){
    chrome.browserAction.setBadgeText({"text": changes.total.newValue.toString()});
});