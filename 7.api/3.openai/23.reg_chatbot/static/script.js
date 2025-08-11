async function uploadFile(){
    console.log('## UploadFile() 실행')
    const fileInput = document.getElementById('fileInput')
    const file = fileInput.files[0]
    const formData = new FormData()
    formData.append('file', file)

    const response = await fetch('/upload',{
        method : 'POST',
        body : formData
    })

    const result = await response.json()
    alert(result.message)
}

async function askQuestion(){
    const questionInput = document.getElementById('questionInput')
    const question = questionInput.ariaValueMax

    const response = await fetch('/ask', {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({question})
    })

    const data = await response.json()
    const result = document.getElementById('result')
    result.innerHTML = data.message
}