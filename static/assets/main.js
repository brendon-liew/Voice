window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;



const recognition = new window.SpeechRecognition();



recognition.lang = "en-US";

recognition.onresult = (e) => {
				analyse( e.results[0][0].transcript.toLowerCase() );
				var cap = e.results[0][0].transcript;
				var running = document.getElementById("resultVoice");
				running.value=cap;
				var ac = document.getElementById("ac");
				ac.value= e.results[0][0].confidence;
				console.log('Confidence: ' + e.results[0][0].confidence);
			       }



recognition.onerror = e => console.error( e );







const go = where =>{

	if( where.match(/forward|backward|left|right/) )

		window.location.href = where;

}



const rules = [

	{rule: /.*go(.*)/, response: 1, action: go }

];



const analyse = msg => {

	btn.disabled = false;

	let response = "I didn't understand";

	let matches;

	for(let i = 0; i < rules.length; i++){

		let r = rules[i];

		matches = r.rule.exec(msg);

		if( matches ){

			response = r.response === 1 ? r.action(matches[1]) : r.response ;

			break;

		}

	}

	say(response);

}



const say = msg => {

	let what = new SpeechSynthesisUtterance(msg);

	what.lang = "en-US";

	speechSynthesis.speak(what);

}



const btn = document.createElement('button');

btn.innerText = "Speak";

var btn2 = document.ElementByID("stopVoice");

btn.onclick = ()=> {

	btn.disabled = true;

	recognition.start();

}
btn2.onclick=()=>{
   btn.disabled = false;
  recognition.stop();
}

//document.body.appendChild(btn);
document.getElementById("test").appendChild(btn);
