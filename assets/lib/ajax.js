loginServer = function (opt,username, password) {
    opt = Object.assign({}, {
        type: 'POST',
        async: true,
        isJson: true
    }, opt || {});

    let xhr, data;
    if (window.XMLHttpRequest) { // Mozilla, Safari, IE7+ ...
        xhr = new XMLHttpRequest();
    } else if (window.ActiveXObject) { // IE 6 and older
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }


    xhr.onreadystatechange = function () {
        // try {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                let res = xhr.responseText;
                opt.isJson && (res = JSON.parse(res));
                opt.success && opt.success(res);
            } else {
                console.log('There was a problem with the request.');
            }
        }
        // } catch (e) {
        //     console.error('Caught Exception: ' + e);
        // }
    }
    xhr.open(opt.type, opt.url, opt.async);
    // Set the Authorization header
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.send(JSON.stringify({
        username: username,
        password: password
    }));
}

window.AJAX = function (opt, token) {
    opt = Object.assign({}, {
        type: 'POST',
        async: true,
        isJson: true
    }, opt || {});

    let xhr, data;
    if (window.XMLHttpRequest) { // Mozilla, Safari, IE7+ ...
        xhr = new XMLHttpRequest();
    } else if (window.ActiveXObject) { // IE 6 and older
        xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }

    if (opt.isJson) {
        data = JSON.stringify(opt.data);
    }


    xhr.onreadystatechange = function () {
        // try {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                let res = xhr.responseText;
                opt.isJson && (res = JSON.parse(res));
                opt.success && opt.success(res);
            } else {
                console.log('There was a problem with the request.');
            }
        }
        // } catch (e) {
        //     console.error('Caught Exception: ' + e);
        // }
    }
    xhr.open(opt.type, opt.url, opt.async);
    // Set the Authorization header
    xhr.setRequestHeader('Authorization', 'Token ' + token);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
    xhr.setRequestHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    xhr.setRequestHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

    xhr.send(data);
}