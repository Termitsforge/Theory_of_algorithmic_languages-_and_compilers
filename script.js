import rpn from "rpn.js"

let inputString = document.querySelector(".input");
let RPN = document.querySelector(".rpn");
let output = document.querySelector(".output");

let btn = document.querySelector('.btn');

btn.onclick = () =>{
    RPN.textContent = new rpn(inputString.value).$outputRpn();
};


