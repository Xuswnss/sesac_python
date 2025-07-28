

document.addEventListener("DOMContentLoaded",()=>{
      const itemInfo = document.getElementById('item-info')
    const itemId = itemInfo.dataset.itemId
    console.log('itemId : ', itemId)
    fetchItems(itemId)
    fetchMonthSales(itemId)
})

function fetchItems(item_id){
    fetch(`/items/api/get-item-detail/${item_id}`)
        .then(res=>res.json())
        .then(data => {
            const resultDiv = document.getElementById('item-result')
            resultDiv.innerHTML = ''   
            console.log(data)
            console.log(data[0])
            data = data[0]
            if(data){
    
                const row = document.createElement('tr')
                row.innerHTML = `
                            <td>${data.name || ''}</td>
                            <td>${data.unit_price || ''}</td>
                `
                resultDiv.appendChild(row)
                
            }else{
                 const row = document.createElement('tr');
                    row.innerHTML = '<td>데이터가 없습니다.</td>';
                    result.appendChild(row);
            }


     
        }
    
    )
}

function fetchMonthSales(item_id){
    fetch(`/items/api/get-months-sales-data/${item_id}`)
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
