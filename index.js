// 这里实现打开摄像头和打开文件管理器来接收图像，上传图像，接收结果后发送结果图像到前端
var body = document.body;

body.addEventListener('click',
    function uploadImg() {
        const formData = new FormData();
        const fileField = document.querySelector('input[type="file"]');
        formData.append("file", fileField.files[0]);

        fetch('122.9.133.29:8080/api/img', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(result => {
                console.log('Success:', result);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
)

