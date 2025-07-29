document.addEventListener('DOMContentLoaded',()=>{
    const orderInfo = document.getElementById('order-info')
    const orderId = orderInfo.dataset.orderId
    console.log('OrderId : ', orderId)
    fetchOrderItems(orderId)
})

function fetchOrderItems(order_id){
    fetch(`/orders/api/get-order-detail/${order_id}`)
        .then(res => res.json())
        .then(data => {
            const result = document.getElementById('result')
            result.innerHTML = ''
            if(data){
                data.forEach(item => {
                    const row = document.createElement('tr')
                    row.innerHTML = `
                     <td>${item.id || ''}</td>
                     <td>${item.order_at || ''}</td>
                     <td>${item.store_id || ''}</td>
                     <td>${item.user_id || ''}</td>
                            
                    `
                    result.append(row)
                });
            }
            console.log(data)
        })
}//end fetchOrderItems(order_id)