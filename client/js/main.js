function drawHistory(){
    const big_div = document.getElementById("history_text")
    big_div.innerHTML = '';
    for (const message of HISTORY) {
        let div = document.createElement('div');
        
        div.className = "message";
        div.innerHTML = `<div class = "data">${message[2]}</div><div class = "text">${message[1]}</div>`;

        big_div.appendChild(div);
    }
}

async function nextHistory() {
  if (HISTORY.length == 0){
      return 
  }
  const res = await fetch('/', {
    method: 'POST',
    body: JSON.stringify({ action: "history", arg: [3, HISTORY[0][0]]}),
  });

  if (!res.ok) {
    return alert(await res.text()); 
  } 
   
  
  for (const message of await res.json()) {
      
    HISTORY.unshift(message);
  }



   drawHistory()
 
}



async function postMessage() {
  const res = await fetch('/', {
    method: 'POST',
    body: JSON.stringify({ action: "+1", arg: NUMBER.value.trim() }),
  });

  if (!res.ok) {
    return alert(await res.text()); 
  }  
  const data = new Date()
  HISTORY.unshift([await res.text(), NUMBER.value.trim(), data])
  drawHistory()
}

const HISTORY = [];


addEventListener("load", async() => {
  const res = await fetch('/', {
    method: 'POST',
    body: JSON.stringify({ action: "history", arg: [3, null]}),
  });
   
  const history = await res.json();
  
  for (const message of history) {
      
    HISTORY.push(message);
  }

  drawHistory()
});
