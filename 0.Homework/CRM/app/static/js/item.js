

document.addEventListener("DOMContentLoaded",()=>{
    fetchItems(1)
})

function fetchItems(page){
    fetch(`/items/api/get-item?page=${page}&per_page=10`)
        .then(res=>res.json())
        .then(data => {
            const resultDiv = document.getElementById('result')
            resultDiv.innerHTML = '' 
        
            console.log(data)
            if(data){
                data.items.slice(1).forEach( item => {
                const row = document.createElement('tr')
                row.innerHTML = `
                            <td><a href='/items/item-detail/${item.id}'>${item.id || ''}</a></td>
                            <td>${item.type || ''}</td>
                            <td>${item.name || ''}</td>
                            <td>${item.unit_price || ''}</td>
                `
                resultDiv.appendChild(row)
                })
            }else{
                 const row = document.createElement('tr');
                    row.innerHTML = '<td>데이터가 없습니다.</td>';
                    result.appendChild(row);
            }


           currentPage = data.page;
                totalPages = data.pages;
                console.log('current-Page :' , data.page, 'total Page:', data.pages)
              updatePaginationControls();     


        }
    
    )
}

 
    function updatePaginationControls() {
    const pageNumbersDiv = document.getElementById('page-numbers');
    pageNumbersDiv.innerHTML = '';
    const pageNumbers = generatePageNumbers(currentPage, totalPages);
    
    pageNumbers.forEach(item => {
        const pageBtn = document.createElement('button');
        pageBtn.textContent = item;
        pageBtn.className = 'page-number';
        
        if (item === currentPage) {
            pageBtn.classList.add('active');
            pageBtn.disabled = true;
        } else {
            pageBtn.onclick = () => fetchItems(item);
        }
        
        pageNumbersDiv.appendChild(pageBtn);
    });
}

function generatePageNumbers(current, total) {
    const delta = 2; 
    const range = [];

    const start = Math.max(1, current - delta);
    const end = Math.min(total, current + delta);

    for (let i = start; i < end; i++) {
        range.push(i);
    }

    return range;
}
