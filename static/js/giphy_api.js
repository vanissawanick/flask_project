var api ="http://api.giphy.com/v1/gifs/search?"; /*search always qith ? */
var apiKey ="&api_key=dc6zaTOxFJmzC";
var query = "&q=rainbow";

function setup(){
	noCanvas();
	var url = api + apiKey + query;
	loadJSON(url, gotData);
}

function gotData(data) {
	println(data.data.[0].images.original.url);
}

function draw(){

}