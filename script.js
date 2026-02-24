console.log("Skeleton Builder app initialized");

document.addEventListener('DOMContentLoaded', () => {
    const bones = document.querySelectorAll('.bone');
    const dropZone = document.getElementById('drop-zone');

    // Future functionality: Drag and drop logic will go here
    bones.forEach(bone => {
        bone.addEventListener('click', () => {
            console.log(`Clicked on ${bone.id}`);
            // Example interaction
            bone.style.borderColor = '#ffffff';
            setTimeout(() => {
                bone.style.borderColor = '#00FFFF';
            }, 500);
        });
    });
});