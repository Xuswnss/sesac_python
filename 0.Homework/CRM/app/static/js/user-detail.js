
document.addEventListener("DOMContentLoaded", () => {
    const userInfoDiv = document.getElementById('user-info');
    const userId = userInfoDiv.dataset.userId;
    console.log('UserID:', userId);
    fetchUser(userId)
    fetchUserOrders(userId)
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
                            <td>${order.id || ''}</td>
                            <td>${order.order_at || ''}</td>
                            <td>${order.store_id || ''}</td>
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