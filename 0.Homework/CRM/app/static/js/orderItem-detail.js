document.addEventListener('DOMContentLoaded',()=>{
    const orderInfo = document.getElementById('order-info')
    const orderId = orderInfo.dataset.orderId
    console.log('OrderId : ', orderId)
    fetchOrderItemsDetail(orderId)
})

function fetchOrderItemsDetail(order_id){
    fetch(`/orderitems/api/get-order-item/${order_id}`)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            const result = document.getElementById('result')
            result.innerHTML = ''
            if(data){
                data.forEach(item => {
                    const row = document.createElement('tr')
                    row.innerHTML = `
                     <td>${item.id || ''}</td>
                     <td><a href = '/orders/order-detail/${item.order_id || ''}'>${item.order_id || ''}</a></td>
                     <td><a href='/items/item-detail/${item.item_id || ''}'>${item.item_id || ''}</a></td>
                     <td>${item.item_name || ''}</td>
                            
                    `
                    result.append(row)
                });
            }
            console.log(data)
        })
}//end fetchOrderItems(order_id)