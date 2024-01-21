fetch('https://baxyqq01ua.execute-api.ap-southeast-2.amazonaws.com/Prod/put', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
  },
})
  .then(response => response.json())
  .then(() => fetch('https://baxyqq01ua.execute-api.ap-southeast-2.amazonaws.com/Prod/get', {
    method: 'GET',  
    headers: {
      'Content-Type': 'application/json',
    },
  }))
  .then(response => response.json())
  .then(data => {
    document.getElementById('visitCount').innerText = data.visitCount;
  })

