
let users = [] // 전역에 저장
document.addEventListener("DOMContentLoaded",()=>{
    const selectedStoreInfo = document.getElementById('selected-store-info')
    const storeId = selectedStoreInfo.dataset.selectedStoreId
    console.log('storeId : ', storeId)
    fetchOrderMenu(storeId)
})




function fetchOrderMenu(store_id){
    fetch(`/stores/api/order-menu/${store_id}`)
    .then(res => res.json())
    .then(data => {
        console.log(data)
        stores = data.store
        users = data.users
        items = data.items
        const resultDiv = document.getElementById('store-result')
            resultDiv.innerHTML =''
        const itemResultDiv = document.getElementById('item-result')
            itemResultDiv.innerHTML =''
        if(stores){
            
            stores.forEach(store => {
                const row = document.createElement('tr')
                row.innerHTML = `
                <td>${store.id}</td>
                <td>${store.type}</td>
                <td>${store.name}</td>
                <td>${store.address}</td>
                `
                resultDiv.appendChild(row)

                
            });
        }

        if(items){
             items.forEach(i => {
                const row = document.createElement('tr')
                row.innerHTML = `
                <td>${i.name}</td>
                <td>${i.type}</td>
                <td>${i.unit_price}</td>
                `
                itemResultDiv.appendChild(row)

                
            });
        }
    // 검색 이벤트 연결
const userSearchInput = document.getElementById('user-search')
    userSearchInput.addEventListener('input', () => {
        const keyword = userSearchInput.value.toLowerCase()
        const filtered = users.filter(user => 
            user.name.toLowerCase().includes(keyword)
        )
        renderUserList(filtered)
    })
    })
}
// ✅ 사용자 목록 렌더링 함수
function renderUserList(userList) {
    const resultDiv = document.getElementById('user-result')
    resultDiv.innerHTML = ''
    userList.forEach(user => {
        const row = document.createElement('tr')
        row.innerHTML = `
            <td>${user.id}</td>
            <td>${user.name}</td>
            <td>${user.gender}</td>
        `
        resultDiv.appendChild(row)
    }) 
}

