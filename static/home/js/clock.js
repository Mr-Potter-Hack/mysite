setInterval(()=>{
    console.log("Testing")
    d = new Date();
    htime = d.getHours();
    mtimes = d.getMinutes();
    stimes = d.getSeconds();
    hrotation = 30*htime + mtimes/2;
    mrotation = 6*mtimes;
    srotation = 6*stimes

    hour.style.transform = `rotate(${hrotation}deg)`;
    minute.style.transform = `rotate(${mrotation}deg)`;
    second.style.transform = `rotate(${srotation}deg)`;

},1000);