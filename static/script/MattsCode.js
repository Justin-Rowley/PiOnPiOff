/*function name to call inside of a button EG: onclick=poweroff()*/
function poweroff() {
    /*Creates a variable called xhr which allows for web requests*/
    var xhr = new XMLHttpRequest();
    /*creates a varible to store json request*/
    var jsonObj = { "power": "off" };
    /*creates the post request/ HTTP type, URL, async (allows the website to keep doing stuff whilst JS in background)*/
    xhr.open("POST", "/background_process", true);
    /*Sets the header*/
    xhr.setRequestHeader('Content-Type', 'application/json');
    /*sends the data to the server*/
    xhr.send(JSON.stringify(jsonObj));

    /*creates a function that runs when its received data*/
    xhr.onload = function() {
        /*takes data from response and stores inside variable*/
        var result = this.responseText;
        /*checks to see if data is as expected*/
        if (result === "done!") {
            /*prints data to console (That Browser Thing Not Flask [F12])*/
            console.info("All Went Well!")
            }
        else {
            console.info("Here Be Dragons!");

        }
    }
}