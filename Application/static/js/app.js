// Fetch the JSON data and console log it
d3.json("/stockdata").then(function (data) {
    console.log(data);
});