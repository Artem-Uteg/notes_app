

async function makeQuery() {
    const res = await fetch('/', {
        method: 'POST',
        body: JSON.stringify({ action: "+1", arg: NUMBER.value.trim() }),
    });

    if (!res.ok) { return; }

    const json = await res.json();

    NUMBER.value = json.answer;
}

