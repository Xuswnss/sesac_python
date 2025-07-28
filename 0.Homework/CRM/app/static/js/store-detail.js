document.addEventListener('DOMContentLoaded',()=>{
    const storeInfo = document.getElementById('store-info')
    const storeId = storeInfo.dataset.storeId
    console.log('storeId : ', storeId)
    fetchStoreDetail(storeId)
    fetchStoreMonthSales(storeId)
})

function fetchStoreDetail(store_id){
    fetch(`/stores/api/get-store-detail/${store_id}`)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            const result = document.getElementById('store-result')
            result.innerHTML = ''
            if(data){
                data.forEach(item => {
                const row = document.createElement('tr')
                row.innerHTML = `
                   <td>${item.name || ''}</td>
                   <td>${item.type || ''}</td>
                   <td>${item.address || ''}</td>
                    `
                result.append(row)
                })
            }
        })
}// end fetchStoreDetail(store_id)

function fetchStoreMonthSales(store_id){
    fetch(`/stores/api/get-store-month-sales/${store_id}`)
        .then(res => res.json())
        .then(data =>{
            console.log('get-data-Month_sales : ', data)
            const resultDiv = document.getElementById('sales-result')
            resultDiv.innerHTML = ''
            if(data){
                data.forEach(e => {
                    const row = document.createElement('tr')
                    row.innerHTML = `
                        <td>${e.date}</td>
                        <td>${e.total_revenue}</td>
                        <td>${e.count}</td>

                    `
                    resultDiv.append(row)
                    
                });
            }
        })
}
