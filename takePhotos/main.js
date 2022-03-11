//let camera_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let click_button = document.querySelector("#click-photo");
let canvas = document.querySelector("#canvas");

let emp_id = document.getElementById("emp_id");
let emp_name = document.getElementById("emp_name");

let total_clicks = 0
let imgArry = []

//Start Camera 
async function startCam(){
let stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
video.srcObject = stream;
}
startCam();

/*
camera_button.addEventListener('click', async function() {
    let stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    video.srcObject = stream;
});
*/
function printname(){
    console.log("Hi   -", emp_id.value, emp_name.value)
}

click_button.addEventListener('click', function() {
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    let image_data_url = canvas.toDataURL('image/jpeg');
    // data url of the image
    //console.log(image_data_url);
    printname()
    total_clicks++;
    if (total_clicks > 10) {
        alert("Uploading Files");
        sendFiles();
    }
    
    imgArry.push(image_data_url);
    make_make_imgs();
    sendFiles();
    // console.log(imgArry);
});




function make_make_imgs() {
    imgContainer = document.getElementById("img-container");
    imgTag = ""
    for (let i = 0; i < imgArry.length; i++) {

        //  "<canvas id="canvas" width="32" height="24"></canvas>"
        imgTag += "<img src=" + imgArry[i] + " width='32' height='24'>"

    }

    imgContainer.innerHTML = imgTag;

}


async function sendFiles() {
    let data = new FormData();

    data.append("employee_id",emp_id.value)
    data.append("employee_name",emp_name.value)
    
    for (var i = 0; i < imgArry.length; i++) {
        //let file = imgArry.item(i);
        data.append('images_' + i, imgArry[i]);
    }

    const config = {
        headers: { 'content-type': 'multipart/form-data' }
    }
    console.log(data, config);
//    const res = await axios.post('http://localhost:3000/api/images', data, config);
    const res = await axios.post('http://localhost:5000/api/images', data, config);

    console.log(res);
}