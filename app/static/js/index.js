const track = document.getElementById("image-track");
const track2 = document.getElementById("name-track");

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

// const track2 = document.getElementById("name-track");

// window2.onmousedown2 = e => {
//     track2.dataset.mouseDownAt = e.clientY;
// }
// window2.onmouseup = () => {
//     track2.dataset.mouseDownAt = "0";
//     track2.dataset.prevPercentage = track2.dataset.percentage;
// }

// window2.onmousemove2 = e => {
//     if(track2.dataset.mouseDownAt === "0") return;

//     const mouseDelta2 = parseFloat(track2.dataset.mouseDownAt) - e.clientY, 
//     maxDelta2 = window2.innerWidth / 2;
    
//     const percentage2 = (mouseDelta2 / maxDelta2) * -100;
//     nextPercentage2 = parseFloat(track2.dataset.prevPercentage2) + percentage2; 
//     Math2.min(nextPercentage2, 0);
//     Math2.max(nextPercentage2, -100); 

//     track2.dataset.percentage2 = nextPercentage2;
    

//     track2.animate({
//         transform: `translate(${nextPercentage2}%, -50%)`
//     }, { duration: 1200, fill: "forwards" });
    
//     for(const name of track2.getElementsByClassName("name")) {
//         name.animate({
//             objectPosition: `${100 + nextPercentage2}% center`
//         }, { duration: 1200, fill:"forwards" });
//     }
// }