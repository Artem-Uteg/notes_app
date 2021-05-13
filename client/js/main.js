function newHistory(){
    const big_div = document.getElementById("history")
    for (const message of HISTORY) {
        let div = document.createElement('div');
        
        div.className = "message";
        div.innerHTML = `<div class = "data">${message[0]}</div><div class = "text">${message[1]}</div>`;

        big_div.appendChild(div);
    }
}

async function makeHistory() {
  const res = await fetch('/', {
    method: 'POST',
    body: JSON.stringify({ action: "next", arg: HISTORY[HISTORY.length-1][2]}),
  });

  if (!res.ok) {
    return alert(await res.text()); 
  }  
    
}



async function makeQuery() {
  const res = await fetch('/', {
    method: 'POST',
    body: JSON.stringify({ action: "+1", arg: NUMBER.value.trim() }),
  });

  if (!res.ok) {
    return alert(await res.text()); 
  }  
  newHistory()
}

const HISTORY = [[' ' ,' ', 0]];


addEventListener("load", async() => {
  const res = await fetch('/', {
    method: 'POST',
    body: JSON.stringify({ action: "history" }),
  });
   
  const history = await res.json();
  
  for (const message of history) {
      HISTORY.push(message);
  }

});
