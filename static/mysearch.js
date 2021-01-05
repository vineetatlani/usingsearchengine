function getResults() {
    var x = document.getElementById("searchbar").value;
    var url = "http://127.0.0.1:5000/search/KtCU5l1TqQEe6Q?title=";
    url = url + x;
    response = fetch(url)
    .then(response =>{
        return (response.json())
    })
    .then(data =>{
        var text = "";
        for (var i = 0; i < data.length; i++) {
          text += data[i] + "<br>";
        }
        document.getElementById("results").innerHTML = text;
    })
}