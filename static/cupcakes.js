"use strict";

const BASE_URL = "http://127.0.0.1:5001/api";
const $cupcakeList = $(".cupcake-list")

async function populateCupcakeList() {
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