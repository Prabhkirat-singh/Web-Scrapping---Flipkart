// Intializating
let search_input = document.querySelector(".search_input");
let svg = document.querySelector("svg");
let product_Template = document.querySelector(".product_Template");

function template(data) {
  for (let i = 0; i < data.products_Name.length; i++) {
    html = `<div class="product_Box_Container">
        <div class="image_Container">
          <img src="${data.url[i]}" alt="Product Image"/>
        </div>
        <div class="products_Info">
           <h3>${data.products_Name[i]}</h3>
            <ul>
              <li>512 Gb Rom</l>
              <li>Camera</li>
              <li>Processor</li>
              <li>Screen</l>
              <li>Insurance</l>
              </ul> 
              </div>
              <h2>${data.products_Price[i]}</h2>
              </div>`;
    product_Template.innerHTML += html;
  }
  console.log(data);
}

svg.addEventListener("click", () => {
  product_Template.innerHTML = "";
  const data = { key: search_input.value };
  // Use fetch API to make a POST request
  fetch("http://192.168.1.109:3000/", {
    method: "POST",
    // mode: "no-cors",
    headers: {
      "Content-Type": "application/json",
      // "Content-Length": 100,
    },
    body: JSON.stringify(data), // Convert tthe data to a JSON sring
  })
    .then((response) => {
      return response.json();
    }) // Parse the JSON response
    .then((data) => {
      template(data); // Print the servers's response in the browser console
    })
    .catch((error) => console.error("error:", error)); // Handle the error
});
