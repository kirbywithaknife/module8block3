advice_url = "https://api.adviceslip.com/advice"

$("#main_header").click(function() {

	$.getJSON(advice_url, function(data){
		advice = data["slip"]["advice"]
		set_secret_message(advice);

	});


});

function set_secret_message(msg) {
	p = $("#second_paragraph")

	p.html(msg)
	p.css("color", "red")
}


$("#third_paragraph").click(function() {
	tp = $("#third_paragraph")

	tp.css("color", "blue")
});


