

function dispatch() {
   let delivery_time_sec = 5;


   console.log("delivery started at " + new Date())

   setTimeout(() => {
    console.log("delivered at " + new Date())
   }, delivery_time_sec * 1000);
}

// dispatch()

const headers = new Headers()
headers.append("Content-Type", "application/json")

const body = {
  "test": "event"
}

const options = {
  method: "POST",
  headers,
  mode: "cors",
  body: JSON.stringify(body),
}

fetch("https://eo60be1f41skhhm.m.pipedream.net", options)
