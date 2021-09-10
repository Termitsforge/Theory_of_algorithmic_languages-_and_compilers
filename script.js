let inputString = document.querySelector(".input");
let rpn = document.querySelector(".rpn");
console.log(inputString.value);
setInterval(()=>{
    rpn.textContent = inputString.value;
},100);

function RPN(string){
    
}