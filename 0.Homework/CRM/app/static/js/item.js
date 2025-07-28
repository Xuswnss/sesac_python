

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
                data.items.forEach( item => {
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

 // #updatePaginationControls
    function updatePaginationControls() {
        const pageNumbersDiv = document.getElementById('page-numbers');
        pageNumbersDiv.innerHTML = '';
        const pageNumbers = generatePageNumbers(currentPage, totalPages);
        
        pageNumbers.forEach(item => {
            if (item === '...') {
                const ellipsis = document.createElement('span');
                ellipsis.textContent = '...';
                ellipsis.className = 'page-ellipsis';
                pageNumbersDiv.appendChild(ellipsis);
            } else {
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
            }
        });
    }
    // #generatePageNumbers
    function generatePageNumbers(current, total) {
    const delta = 2; // 현재 페이지 앞뒤로 표시할 범위
    const range = [];
    
    const left = current - delta;
    const right = current + delta;

    const showLeftEllipsis = left > 2;
    const showRightEllipsis = right < total - 1;

    range.push(1); // Always show the first page

    if (showLeftEllipsis) {
        range.push('...');
    }

    for (let i = Math.max(2, left); i <= Math.min(total - 1, right); i++) {
        range.push(i);
    }

    if (showRightEllipsis) {
        range.push('...');
    }

    if (total > 1) {
        range.push(total); // Always show the last page
    }

    return range;
}

   