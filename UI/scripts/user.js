function signup() {
    var url = 'http://127.0.0.1:5000/api/v1/auth/signup';
    var Pusername = document.getElementById("username1").value;
    var Ppassword = document.getElementById("password1").value;
    // var password2 = document.getElementById('password2').value;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: Pusername, password: Ppassword
        })
    })
    .then(function (response) {
        return response.json();
    })
    .then(function(data){
        if (data.status_code == 201){
            document.getElementById("call1").innerHTML = "Created Succesfully";
            window.location.href = "/index.html"
        } else {
            document.getElementById("call").innerHTML = "Fail : username and password should be provided and *WITH NOT* less than 5 values *EACH*!. Please Avoid such ^{\\s|\\S}*{\\S}+{\\s|\\S}*$ in your username";
            }
    })
    .catch(function (error) {  
        console.log('Request failure: ', error);  
    });
}
function signin() {}