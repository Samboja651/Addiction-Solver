const obj1 = document.getElementById('obj1')

console.log(obj1)

function changeColor(){
    obj1.style.backgroundColor = 'yellow';
}

obj1.addEventListener('mouseover', changeColor, false)
// obj1.removeEventListener('mouseover', changeColor, false)
