window.addEventListener('load', () => {
    const canvas = document.querySelector("#canvas");
    const ctx = canvas.getContext("2d");

    //resizing
    canvas.height = 500;
    canvas.width = 500;


    //Variables
    let painting = false;

    function startPosition(e){
        painting = true;
        draw(e);
    }

    function finishedPosition(){
        painting = false;
        ctx.beginPath();
        toImage();
    }

    function draw(e){
        if(!painting) return;
        ctx.lineWidth = 60;
        ctx.lineCap = 'round';

        ctx.lineTo(e.clientX, e.clientY);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(e.clientX, e.clientY);
    }

    function toImage(){
        var dataURL = canvas.toDataURL();
        document.getElementById('canvasImg').src = dataURL;
    }


    //Event Listeners
    canvas.addEventListener('mousedown', startPosition);
    canvas.addEventListener('mouseup', finishedPosition);
    canvas.addEventListener('mousemove', draw);
    // btn.addEventListener('onclick', send_data);

});






