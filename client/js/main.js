async function makeQuery() {
  const res = await fetch('/', {
    method: 'POST',
    body: JSON.stringify({ action: "+1", arg: NUMBER.value.trim() }),
  });

  if (!res.ok) {
    return alert(await res.text()); 
  }  
}

addEventListener("load", async() => {
  const res = await fetch('/', {
    method: 'POST',
    body: JSON.stringify({ action: "history" }),
  });
   
  const history = await res.json();
  for (const message of history) {
    document.getElementById('history').innerHTML += "\r\n" +`${message[1]}` +' '+`${message[2]}`+' ';
  }

});
