console.log("Skeleton Builder app initialized");

document.addEventListener('DOMContentLoaded', () => {
    // Initialize Draggable Bones
    interact('.draggable-bone').draggable({
        inertia: true,
        autoScroll: true,
        modifiers: [
            interact.modifiers.restrictRect({
                restriction: 'body',
                endOnly: true
            })
        ],
        listeners: {
            start: dragStartListener,
            move: dragMoveListener,
            end: dragEndListener
        }
    });

    // Initialize Drop Zones
    interact('.bone-outline').dropzone({
        accept: '.draggable-bone',
        overlap: 'center',
        ondragenter: function (event) {
            const draggableElement = event.relatedTarget;
            const dropzoneElement = event.target;

            // Only glow if it's the correct bone
            if (isMatch(draggableElement, dropzoneElement)) {
                dropzoneElement.classList.add('drop-target-active');
            }
        },
        ondragleave: function (event) {
            event.target.classList.remove('drop-target-active');
        },
        ondrop: function (event) {
            const bone = event.relatedTarget;
            const outline = event.target;

            if (isMatch(bone, outline)) {
                snapToTarget(bone, outline);
                outline.classList.remove('drop-target-active');
            }
        }
    });
});

function dragStartListener(event) {
    const target = event.target;

    // Prevent interaction if already placed (double safety)
    if (target.classList.contains('placed-bone')) return;

    // Create a placeholder to maintain layout in the bone yard
    const rect = target.getBoundingClientRect();
    const placeholder = document.createElement('div');
    placeholder.className = 'bone-placeholder';
    placeholder.style.width = rect.width + 'px';
    placeholder.style.height = rect.height + 'px';

    // Copy computed margins to placeholder
    const computedStyle = window.getComputedStyle(target);
    placeholder.style.margin = computedStyle.margin;
    placeholder.style.display = computedStyle.display;
    placeholder.style.flex = computedStyle.flex;

    target.parentNode.insertBefore(placeholder, target);
    target.dataset.placeholderId = 'placeholder-' + Date.now();
    placeholder.id = target.dataset.placeholderId;

    // Switch to fixed positioning to escape overflow containers
    target.style.position = 'fixed';
    target.style.left = rect.left + 'px';
    target.style.top = rect.top + 'px';
    target.style.width = rect.width + 'px';
    target.style.height = rect.height + 'px';
    target.style.zIndex = '1000';
    target.style.margin = '0';

    // Reset any transform
    target.style.transform = 'none';
    target.setAttribute('data-x', 0);
    target.setAttribute('data-y', 0);
}

function dragMoveListener(event) {
    const target = event.target;
    // Keep the dragged position in the data-x/data-y attributes
    const x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx;
    const y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

    // Translate the element
    target.style.transform = `translate(${x}px, ${y}px)`;

    // Update the posiion attributes
    target.setAttribute('data-x', x);
    target.setAttribute('data-y', y);
}

function dragEndListener(event) {
    const target = event.target;

    // If the bone was successfully placed, it will have the 'placed-bone' class.
    // If not, we need to revert it to the bone yard.
    if (!target.classList.contains('placed-bone')) {
        revertBone(target);
    }
}

function isMatch(bone, outline) {
    if (!bone || !outline) return false;
    const bonePart = bone.id.replace('bone-', '');
    const outlinePart = outline.id.replace('outline-', '');
    return bonePart === outlinePart;
}

function snapToTarget(bone, outline) {
    // Remove the placeholder from the bone yard
    const placeholderId = bone.dataset.placeholderId;
    const placeholder = document.getElementById(placeholderId);
    if (placeholder) {
        placeholder.remove();
    }

    // Move the bone to the outline container
    outline.appendChild(bone);

    // Apply the placed-bone class to lock it and style it
    bone.classList.add('placed-bone');

    // Clean up inline styles used for dragging
    bone.style.position = 'absolute';
    bone.style.left = '0';
    bone.style.top = '0';
    bone.style.width = '100%';
    bone.style.height = '100%';
    bone.style.transform = 'none';
    bone.style.zIndex = '';
    bone.style.margin = '0';

    // Remove drag data attributes
    bone.removeAttribute('data-x');
    bone.removeAttribute('data-y');
    bone.removeAttribute('data-placeholder-id');

    // Disable dragging for this bone
    interact(bone).unset();
}

function revertBone(bone) {
    const placeholderId = bone.dataset.placeholderId;
    const placeholder = document.getElementById(placeholderId);

    if (placeholder) {
        // Put the bone back where the placeholder is
        placeholder.parentNode.replaceChild(bone, placeholder);

        // Reset all styles to return to original state
        bone.style.position = '';
        bone.style.left = '';
        bone.style.top = '';
        bone.style.width = '';
        bone.style.height = '';
        bone.style.zIndex = '';
        bone.style.margin = '';
        bone.style.transform = '';

        bone.removeAttribute('data-x');
        bone.removeAttribute('data-y');
        bone.removeAttribute('data-placeholder-id');
    }
}
