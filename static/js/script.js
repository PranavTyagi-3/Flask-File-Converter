$(document).ready(function() {
  function setFileInputSize() {
    var height = $("#upload_ic").height();
    var width = $("#upload_ic").width();
    $("#fileInput").height(height);
    $("#fileInput").width(width);
  }
  
  setFileInputSize();
  $(window).resize(setFileInputSize);
});

var dropZone = document.getElementById("upload_ic");
var fileInput = document.getElementById("fileInput");

dropZone.addEventListener("dragenter", function(e) {
  e.stopPropagation();
  e.preventDefault();
});

dropZone.addEventListener("dragover", function(e) {
  e.stopPropagation();
  e.preventDefault();
});

dropZone.addEventListener("drop", function(e) {
  e.stopPropagation();
  e.preventDefault();
  fileInput.files = e.dataTransfer.files;
});

var fileInput = document.getElementById("fileInput");
var selectedFiles = document.getElementById("selectedFiles");

fileInput.addEventListener("change", function() {
  var files = fileInput.files;
  if (files.length > 0) {
    selectedFiles.innerHTML = "";
    for (var i = 0; i < files.length; i++) {
      selectedFiles.innerHTML += files[i].name + "<br>";
    }
  } else {
    selectedFiles.innerHTML = "No files selected";
  }
});


document.getElementById("fileForm").addEventListener("submit", function (event) {
    event.preventDefault();
  
    var fileInput = document.getElementById("fileInput");
    var formData = new FormData();
  
    formData.append("file", fileInput.files[0]);
  
    var xhr = new XMLHttpRequest();
    xhr.open("POST", window.location.pathname, true);
  
    xhr.upload.onprogress = function (event) {
      var percentage = Math.floor((event.loaded / event.total) * 100);
      document.getElementById("progressDiv").style.width = percentage+"%";
      //document.getElementById("uploadProgress").value = percentage;
      document.getElementById("uploadPercentage").innerHTML = percentage + "%";
    };
  
    xhr.onload = function () {
      if (xhr.status === 200) {
        // File upload complete, show the success div and hide the progress div
        document.getElementById("successDiv").style.display = "block";
        document.getElementById("progressDiv").style.display = "none";
        myMove();
      } else {
        console.error("File upload failed");
      }
    };
  
    document.getElementById("progressDiv").style.display = "block";
    xhr.send(formData);
  });


var upload_h = null;
function myMove() {
  document.getElementById("fileInput").style.display="None";
  document.getElementById("upload_icon").style.display="None";
  var h = document.getElementById("upload_ic");   
  var start_h=h.offsetHeight;
  clearInterval(upload_h);
  upload_h = setInterval(frame, 10);
  function frame() {
    if ( start_h == 0) {
      clearInterval(upload_h);
    } else {
      start_h--; 
      h.style.height = start_h + 'px'; 
    }
  }
}

async function conv() {
  document.getElementById("wait_conversion").style.display='block';

  const response = await fetch("/downl" + window.location.pathname + "&&" + fileInput.files[0].name);
  const blob = await response.blob();
  if (blob.type=='text/html'){
    window.location.href = '/';
  } else {
    const a = document.createElement('a');
    a.style.display = 'none';
    document.body.appendChild(a);
    console.log(fileInput.files[0].name.split(".")[0])
    const url = window.URL.createObjectURL(blob);
    a.href = url;
    a.download = fileInput.files[0].name.split(".")[0];
    a.click();

    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);

    document.getElementById("wait_conversion").style.display='none';
    document.getElementById("thank_you").style.display='block';
  }
}

