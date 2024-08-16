function translateText() {
    var textToTranslate = document.getElementById("entertext").value;

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'text-to-be-translated': textToTranslate,
        }),
    })
    .then(response => response.json())
    .then(data => {
        displayTranslatedImages(data.images);
    })
    .catch(error => console.error('Error:', error));
}

function displayTranslatedImages(imageDataList) {
    var translatedImagesDiv = document.getElementById('modalBody');
    translatedImagesDiv.innerHTML = '';

    imageDataList.forEach(function(imageData) {
        var imgElement = document.createElement('img');
        imgElement.src = 'data:image/jpeg;base64,' + imageData;
        translatedImagesDiv.appendChild(imgElement);
    });
}

function displayTranslatedImages(imageDataList) {
    var translatedImagesDiv = document.getElementById('modalBody');
    translatedImagesDiv.innerHTML = '';

    imageDataList.forEach(function(imageData) {
        var imgElement = document.createElement('img');
        imgElement.src = 'data:image/jpeg;base64,' + imageData;
        imgElement.classList.add('img-fluid'); // Add Bootstrap's img-fluid class for responsive images
        translatedImagesDiv.appendChild(imgElement);
    });

    // Trigger the modal
    var translatedImagesModal = new bootstrap.Modal(document.getElementById('translatedImagesModal'));
    translatedImagesModal.show();
}

