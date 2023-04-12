// image track
const track = document.getElementById("image-track");

// name track
const track2 = document.getElementById("name-track");


// if user is on mobile device, execute follwing code
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) {

    window.ontouchstart = e => {
        track.dataset.touchstart = e.touches[0].clientX;
        track2.dataset.touchstart = e.touches[0].clientY;
    }
    
    window.ontouchend = () => {
        track.dataset.touchstart = "0";
        track.dataset.prevPercentage = track.dataset.percentage;
    
        track2.dataset.touchstart = "0";
        track2.dataset.prevPercentage = track2.dataset.percentage2;
    }
    
    window.ontouchmove = e => {
        if(track.dataset.touchstart === "0") return;
        if(track2.dataset.touchstart === "0") return;
    
        const touchDelta = parseFloat(track.dataset.touchstart) - e.touches[0].clientX, 
        maxDelta = window.innerWidth / 0.3;
        const touchDelta2 = parseFloat(track.dataset.touchstart) - e.touches[0].clientX, 
        maxDelta2 = window.innerWidth / 0.3;
        
        const percentage = (touchDelta / maxDelta) * -100;
        nextPercentage = parseFloat(track.dataset.prevPercentage) + percentage; 
        Math.min(nextPercentage, 0);
        Math.max(nextPercentage, -100); 
    
        const percentage2 = (touchDelta2 / maxDelta2) * -100;
        nextPercentage2 = parseFloat(track2.dataset.prevPercentage) + percentage2; 
        Math.min(nextPercentage2, 0);
        Math.max(nextPercentage2, -100); 
    
        track.dataset.percentage = nextPercentage;
        track2.dataset.percentage2 = nextPercentage2;
        
    
        track.animate({
            transform: `translate(${nextPercentage}%, -50%)`
        }, { duration: 1200, fill: "forwards" });
    
        track2.animate({
            transform: `translate(${nextPercentage2}%, -50%)`
        }, { duration: 1200, fill: "forwards" });
        
        for(const image of track.getElementsByClassName("image")) {
            image.animate({
                objectPosition: `${100 + nextPercentage}% center`
            }, { duration: 100, fill:"forwards" });
        }
    
        for(const name of track2.getElementsByClassName("name")) {
            name.animate({
                objectPosition: `${100 + nextPercentage2}% center`
            }, { duration: 100, fill:"forwards" });
        }
    }
} else {
    window.onmousedown = e => {
        track.dataset.mouseDownAt = e.clientX;
        track2.dataset.mouseDownAt = e.clientY;
    }
    
    window.onmouseup = () => {
        track.dataset.mouseDownAt = "0";
        track.dataset.prevPercentage = track.dataset.percentage;
    
        track2.dataset.mouseDownAt = "0";
        track2.dataset.prevPercentage = track2.dataset.percentage2;
    }
    
    window.onmousemove = e => {
        if(track.dataset.mouseDownAt === "0") return;
        if(track2.dataset.mouseDownAt === "0") return;
    
        const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX, 
        maxDelta = window.innerWidth / 0.3;
        const mouseDelta2 = parseFloat(track.dataset.mouseDownAt) - e.clientX, 
        maxDelta2 = window.innerWidth / 0.3;
        
        const percentage = (mouseDelta / maxDelta) * -100;
        nextPercentage = parseFloat(track.dataset.prevPercentage) + percentage; 
        Math.min(nextPercentage, 0);
        Math.max(nextPercentage, -100); 
    
        const percentage2 = (mouseDelta2 / maxDelta2) * -100;
        nextPercentage2 = parseFloat(track2.dataset.prevPercentage) + percentage2; 
        Math.min(nextPercentage2, 0);
        Math.max(nextPercentage2, -100); 
    
        track.dataset.percentage = nextPercentage;
        track2.dataset.percentage2 = nextPercentage2;
        
    
        track.animate({
            transform: `translate(${nextPercentage}%, -50%)`
        }, { duration: 1200, fill: "forwards" });
    
        track2.animate({
            transform: `translate(${nextPercentage2}%, -50%)`
        }, { duration: 1200, fill: "forwards" });
        
        for(const image of track.getElementsByClassName("image")) {
            image.animate({
                objectPosition: `${100 + nextPercentage}% center`
            }, { duration: 100, fill:"forwards" });
        }
    
        for(const name of track2.getElementsByClassName("name")) {
            name.animate({
                objectPosition: `${100 + nextPercentage2}% center`
            }, { duration: 100, fill:"forwards" });
        }
    }
    
}
