
document.addEventListener("DOMContentLoaded", () => {
    const userInfoDiv = document.getElementById('user-info');
    const userId = userInfoDiv.dataset.userId;
    console.log('UserID:', userId);
    fetchUser(userId)
    fetchUserOrders(userId)
    fetchRegularStore(userId)
    fetchRegularGoods(userId)
})

function fetchUser(user_id){
    fetch(`/users/user-detail/api/get-user/${user_id}`)
        .then(res => res.json())
        .then(data => {
            console.log('data : ', data)
            const result = document.getElementById('user-result')
            result.innerHTML =''
            if(data){
                Array(data).forEach(user => {
                    const row = document.createElement('tr')
                     row.innerHTML = `
                            <td><a href="/users/user-detail/${user.id}">${user.id || ''}</a></td>
                            <td>${user.name || ''}</td>
                            <td>${user.age || ''}</td>
                            <td>${user.gender || ''}</td>
                            <td>${user.birthday || ''}</td>
                            <td>${user.address || ''}</td>
                        `;
                    result.appendChild(row)
                });
            }else{
                const row = document.createElement('tr');
                    row.innerHTML = '<td>데이터가 없습니다.</td>';
                    result.appendChild(row);
            }


        })
   
}// end fetchUser()


function fetchUserOrders(user_id){
    console.log(user_id)
    fetch(`/users/user-detail/api/order-list/${user_id}`)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            const result = document.getElementById('order_result')
            result.innerHTML = '';
            if(data){
                data.forEach(order => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                            <td><a href="/orderitems/orderItem-detail/${order.id}">${order.id || ''}</a></td>
                            <td>${order.order_at || ''}</td>
                            <td><a href ='/stores/store-detail/$${order.store_id || ''}'>${order.store_id || ''}</a></td>
                    `;
                    result.appendChild(row)
                })
            }else {
                    let row = document.createElement('tr');
                    row.innerHTML = '<td>데이터가 없습니다.</td>';
                    result.appendChild(row);
                }

        })
}// end fetchUserOrders

function fetchRegularStore(user_id){
    fetch(`/users/user-detail/api/get-regular-store/${user_id}`)
        .then(res => res.json())
        .then(data =>{
            console.log('store - data :',data)
            const resultDiv = document.getElementById('regular-stores')
            resultDiv.innerHTML = ''
            if(data){
                const stores = data.sort((a, b) => b.frequency - a.frequency).slice(0, 5);
                stores.forEach(e => {
                    const li = document.createElement('ul')
                    li.innerHTML = `
                        <li>${e.store_name} (${e.frequency}번 방문)</li>
                    `
                    resultDiv.appendChild(li)
                    
                });
            }
        })
}

function fetchRegularGoods(user_id){
    fetch(`/users/user-detail/api/get-regular-goods/${user_id}`)
        .then(res => res.json())
        .then(data =>{
            console.log(data)
            const resultDiv = document.getElementById('regular-goods')
            resultDiv.innerHTML =''
            if(data){
                const goods = data.sort((a, b) => b.frequency - a.frequency).slice(0, 5);
                goods.forEach(e => {
                    const li = document.createElement('ul')
                    li.innerHTML = `
                        <li>${e.item_name} (${e.frequency}번 주문)</li>
                    `
                    resultDiv.appendChild(li)
                    
                });
            }
        })
}