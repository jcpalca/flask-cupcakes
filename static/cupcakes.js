"use strict";

const BASE_URL = "http://127.0.0.1:5001/api";
const $cupcakeList = $(".cupcake-list")
const $cupcakeForm = $("#add-cupcake")
//new controller calls getCupcakes and populateList
async function populateCupcakeList() {
    $cupcakeList.empty()
    
    //move to controller function
    let cupcakes = await getCupcakes();
    
    for (let cupcake of cupcakes) {
        
        //make into it's own function
        let $listItem = $(
            `
            <div id="${cupcake.id}">
            <li>
            Flavor: ${cupcake.flavor}
            <br>
            Size: ${cupcake.size}
            <br>
            Rating: ${cupcake.rating}
            </li>
            <img src="${cupcake.image}" width="200px">
            </div>
            `
        );
        $cupcakeList.append($listItem);
    }

}

async function getCupcakes() {
    let response = await axios.get(`${BASE_URL}/cupcakes`);

    return response.data.cupcakes;
}

async function addNewCupcake(evt) {
    console.debug("addNewCupcake ran!")
    evt.preventDefault();

    let flavor = $("#flavor").val()
    let size = $("#size").val()
    let rating = $("#rating").val()
    let image = $("#image-url").val()

    let response = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        size,
        rating,
        image,
    })

    await populateCupcakeList();
}

$cupcakeForm.on("submit", addNewCupcake);

populateCupcakeList();
