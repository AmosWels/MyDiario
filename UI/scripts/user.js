function signup() {
    var url = 'http://127.0.0.1:5000/api/v1/auth/signup';
    var Pusername = document.getElementById("username1").value;
    var Ppassword = document.getElementById("password1").value;
    var status_code = 201 || 200;
    // var password2 = document.getElementById('password2').value;
    fetch(url, {
        method: 'POST', cache: 'reload',
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
        .then(function (response) {
            if (response.ok) {
                document.getElementById("call").innerHTML = "Created Succesfully";
                window.location = "./index.html"
            } else {
                document.getElementById("call").innerHTML = "Fail : username and password should be provided and *WITH NOT* less than 5 values *EACH*!. Please Avoid such ^{\\s|\\S}*{\\S}+{\\s|\\S}*$ in your username";
            }
        })
        .catch(function (error) {
            console.log('Request failure: ', error);
        });
}
function login() {
    var url = 'http://127.0.0.1:5000/api/v1/auth/login';
    var Pusername = document.getElementById("uname").value;
    var Ppassword = document.getElementById("upassword").value;
    var status_code = 201 || 200;
    fetch(url, {
        method: 'POST', cache: 'reload',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: Pusername, password: Ppassword
        })
    })
        .then(function (Response) {
            return Response.json();
        })
        .then(function (Response) {
            if (Response.status == 201) {
                window.localStorage.setItem('Bearer', Response.token);
                window.location ='./viewdiaries.html';
            } else {
                document.getElementById("call").innerHTML = "Fail : Wrong Credentials";
            }
        })
        .catch(function (error) {
            console.log('Request failure: ', error);
        });
 }