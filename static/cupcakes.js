"use strict";

const BASE_URL = "http://127.0.0.1:5001/api";
const $cupcakeList = $(".cupcake-list")
const $cupcakeForm = $(".add-cupcake")

async function populateCupcakeList() {
    $cupcakeList.empty()
    let cupcakes = await getCupcakes();
    for (let cupcake of cupcakes) {
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

await populateCupcakeList();
