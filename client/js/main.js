async function makeQuery() {
const res = await fetch('/', {
method: 'POST',
body: JSON.stringify({ action: "+1", arg: NUMBER.value.trim() }),
});

if (!res.ok) {
  if (res.status == 418){
    document.getElementById('ok').innerHTML="Плохая чиселка, попробуйте другую.";
    document.getElementById('ok').style.color="red"; 
}

  if (res.status == 500){
    document.getElementById('ok').innerHTML="Не чиселка, попробуйте чиселку.";
    document.getElementById('ok').style.color="red";
}

  return; } 

document.getElementById('ok').innerHTML="Все ок!";

document.getElementById('ok').style.color="green";

const json = await res.json();

NUMBER.value = json.answer;

}