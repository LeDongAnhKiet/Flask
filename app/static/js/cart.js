function add2Cart(id, name, price){
    fetch('/api/cart', {
        method: "post",
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => res.json()).then(data) => {
        console.info(data)
        let d = document.getElementsByClassName("cart-counter")
        for (int i = 0; i< d.length; i++)
            d[i].innerText = data.total_quantity
    })
}
function updateCart(productId, obj){
fetch('/api/cart/${ productId }', {
        method: "put",
        body: JSON.stringify({
            "quantity":obj.value
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => res.json()).then(data) => {
        let d = document.getElementsByClassName("cart-counter")
        for (int i = 0; i< d.length; i++)
            d[i].innerText = data.total_quantity
        let a = document.getElementsByClassName("cart-amount")
        for (int i = 0; i< a.length; i++)
            a[i].innerText = data.total_amount.toLocaleString("en-US")
    }).catch(err => console.error(err))
}
function delCart(productId, obj){
    if (confirm("Chắc xóa ko!") == true){
        fetch('/api/cart/${ productId }',{
        method: "delete"
    }).then(res => res.json()).then(data) => {
        let d = document.getElementsByClassName("cart-counter")
        for (int i = 0; i< d.length; i++)
            d[i].innerText = data.total_quantity
        let a = document.getElementsByClassName("cart-amount")
        for (int i = 0; i< a.length; i++)
            a[i].innerText = data.total_amount.toLocaleString("en-US")
        let e = document.getElementById('cart${productId}')
        e.style.display = "none"
    }).catch(err => console.error(err))
    }
}