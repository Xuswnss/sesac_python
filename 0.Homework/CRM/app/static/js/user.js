
    let currentPage = 1;
    let totalPages = 1;
    let error = document.getElementById('error')

    const search_form = document.getElementById('user-select-form')
    document.addEventListener("DOMContentLoaded", () => {
        fetchUsers(1); // 1페이지부터 시작
    });

    // #fetchUser (pagination)
    function fetchUsers(page = 1, name = '', gender = '') {
         currentPage = page;
        currentName = name;
        currentGender = gender;
        let url = '';
        // 검색 조건 있으면 search API 호출, 없으면 기본 API 호출
        if (name || gender) {
        url = `/users/api/search?name=${encodeURIComponent(name)}&gender=${encodeURIComponent(gender)}&page=${page}&per_page=10`;
        } else {
        url = `/users/api?page=${page}&per_page=10`;
        }
        fetch(url)
            .then(res => {
                if (!res.ok) {
                    console.log(res.status)
                }
                return res.json();
            })
            .then(data => {
                const result = document.getElementById('result');
                result.innerHTML = ''; // 기존 내용 초기화
                console.log('data : ', data)

                if (data.users && data.users.length > 0) {
                    data.users.slice(1).forEach(user => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td><a href="/users/user-detail/${user.id}">${user.id || ''}</a></td>
                            <td>${user.name || ''}</td>
                            <td>${user.age || ''}</td>
                            <td>${user.gender || ''}</td>
                            <td>${user.birthday || ''}</td>
                            <td>${user.address || ''}</td>
                        `;
                        result.appendChild(row);
                    });
                } else {
                    const row = document.createElement('tr');
                    row.innerHTML = '<td>데이터가 없습니다.</td>';
                    result.appendChild(row);
                }

                currentPage = data.page || 1;
                if (data.pages) {
                    totalPages = data.pages;
                } else if (data.total && data.per_page) {
                     totalPages = Math.ceil(data.total / data.per_page);
                } else {
                         totalPages = 1;
                }

                
                updatePaginationControls();
                updatePageInfo()
            })
            .catch(error => {
                console.log('error : ', error)
            });
    }
 // 이전 버튼
    function updatePaginationControls() {
    const paginationContainer = document.getElementById('page-numbers');
    paginationContainer.innerHTML = '';
    
    // 이전 버튼
    const prevBtn = document.createElement('button');
    prevBtn.innerHTML = '&laquo;';
    prevBtn.className = 'page-btn prev-btn';
    prevBtn.disabled = currentPage === 1;
    if (currentPage > 1) {
        prevBtn.onclick = () => fetchUsers(currentPage - 1, currentName, currentGender);
    }
    paginationContainer.appendChild(prevBtn);
    
    // 페이지 번호들
    const pageNumbers = generatePageNumbers(currentPage, totalPages);
    pageNumbers.forEach(pageNum => {
        const pageBtn = document.createElement('button');
        pageBtn.innerHTML = pageNum;
        pageBtn.className = 'page-btn';
        
        if (pageNum === currentPage) {
            pageBtn.classList.add('active');
        } else {
            pageBtn.onclick = () => fetchUsers(pageNum , currentName, currentGender);
        }
        
        paginationContainer.appendChild(pageBtn);
    });
    
    // 다음 버튼
    const nextBtn = document.createElement('button');
    nextBtn.innerHTML = '&raquo;';
    nextBtn.className = 'page-btn next-btn';
    nextBtn.disabled = currentPage === totalPages;
    if (currentPage < totalPages) {
        nextBtn.onclick = () => fetchUsers(currentPage +1, currentName, currentGender);
    }
    paginationContainer.appendChild(nextBtn);
}

// 페이지 번호 생성
function generatePageNumbers(current, total) {
    const pages = [];
    const maxVisible = 7;
    
    if (total <= maxVisible) {
        // 전체 페이지가 maxVisible 이하면 모든 페이지 표시
        for (let i = 1; i <= total; i++) {
            pages.push(i);
        }
    } else {
        // 첫 페이지는 항상 표시
        pages.push(1);
        
        const halfVisible = Math.floor((maxVisible - 2) / 2); // 첫/마지막 페이지 제외한 가운데 영역
        let start = Math.max(2, current - halfVisible);
        let end = Math.min(total - 1, current + halfVisible);
        
        // 가운데 영역이 maxVisible-2 개가 되도록 조정
        const middleCount = maxVisible - 2;
        if (end - start + 1 < middleCount) {
            if (start === 2) {
                end = Math.min(total - 1, start + middleCount - 1);
            } else if (end === total - 1) {
                start = Math.max(2, end - middleCount + 1);
            }
        }
        
        // 가운데 페이지들 추가
        for (let i = start; i <= end; i++) {
            if (i !== 1 && i !== total && !pages.includes(i)) {
                pages.push(i);
            }
        }
        
        // 마지막 페이지는 항상 표시 (첫 페이지와 다른 경우만)
        if (total > 1) {
            pages.push(total);
        }
    }
    
    return pages;
}

// 페이지 정보 표시
function updatePageInfo() {
    const pageInfo = document.getElementById('page-info');
    if (pageInfo) {
        // 현재 페이지 / 전체 페이지 형태로 표시
        pageInfo.innerHTML = `${currentPage} / ${totalPages}`;

    }
}



    search_form.addEventListener('submit',(e)=>{
        e.preventDefault()
        currentName = document.getElementById('name-input').value.trim();
        currentGender = document.getElementById('gender-select-box').value;
        currentPage = 1;  // 검색할 때는 페이지 1로 초기화
    fetchUsers(currentPage, currentName, currentGender);
    })
    

