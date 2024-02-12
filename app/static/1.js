let fin = document.getElementById('fin')
let fin2 = document.getElementById('fin2')
let forma = document.getElementById('forma')
fin.onclick = f1
fin2.onclick = f2

function f1(){
    forma.hidden = false

}

function f2(){
    let adres = document.getElementById('adres').value
    let name = document.getElementById('name').value
    let tel = document.getElementById('tel').value
    if (adres&&name&&tel){
        //alert('ok')
        fetch('/cart/pobeda/'+adres,
            {
        method:'POST',
        headers: {
      //      'Content-Type':'application/json',
            'X-CSRFToken': csrf_token,
        },
     //   body: JSON.stringify({message:adres}),
                body:adres,

    }
        )
    }
    else {
        alert('ne zapolneno')
    }

}

