console.log("Skeleton Builder app initialized");

let startTime;
let timerInterval;
let successfulDrops = 0;
let isGameActive = false;

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

    // Initialize Play Again Button
    const playAgainBtn = document.getElementById('play-again-btn');
    if (playAgainBtn) {
        playAgainBtn.addEventListener('click', resetGame);
    }
});

function dragStartListener(event) {
    const target = event.target;

    // Prevent interaction if already placed (double safety)
    if (target.classList.contains('placed-bone')) return;

    // Start Timer on first interaction
    if (!isGameActive && successfulDrops < 6) {
        startTimer();
    }

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

    // Enforce strict matching: The bone part must exactly match the outline part.
    // e.g., 'left-arm' matches 'left-arm', but not 'right-arm'.
    const match = bonePart === outlinePart;

    if (!match) {
        console.log(`Mismatch: ${bone.id} cannot be dropped on ${outline.id} - Snap back enforced.`);
    } else {
        console.log(`Match: ${bone.id} dropped on ${outline.id}`);
    }

    return match;
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

    // NOTE: Removed interact(bone).unset() to allow easier resetting.
    // The .placed-bone class and check in dragStartListener handles disabling interaction.

    // Check Win Condition
    successfulDrops++;
    if (successfulDrops === 6) {
        winGame();
    }
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

// --- Timer & Game Logic ---

function startTimer() {
    if (isGameActive) return;
    isGameActive = true;
    startTime = Date.now();
    // Clear any existing interval just in case
    clearInterval(timerInterval);
    timerInterval = setInterval(updateTimer, 100);
}

function stopTimer() {
    clearInterval(timerInterval);
    isGameActive = false;
}

function updateTimer() {
    const elapsedTime = Date.now() - startTime;
    const timerDisplay = document.getElementById('game-timer');
    if (timerDisplay) {
        timerDisplay.textContent = formatTime(elapsedTime);
    }
}

function formatTime(ms) {
    const totalSeconds = Math.floor(ms / 1000);
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function winGame() {
    stopTimer();
    const finalTimeMs = Date.now() - startTime;
    const finalTimeString = formatTime(finalTimeMs);

    // Save High Score
    const savedBest = localStorage.getItem('skeletonBuilderBestTime');
    let bestTimeMs = savedBest ? parseInt(savedBest) : Infinity;

    if (finalTimeMs < bestTimeMs) {
        bestTimeMs = finalTimeMs;
        localStorage.setItem('skeletonBuilderBestTime', bestTimeMs);
    }

    // Update Modal
    document.getElementById('final-time').textContent = finalTimeString;
    document.getElementById('best-time').textContent = formatTime(bestTimeMs);

    // Show Modal
    const modal = document.getElementById('victory-modal');
    modal.style.display = 'flex';
    // Small delay to allow display:flex to apply before adding visible class for transition
    setTimeout(() => {
        modal.classList.add('visible');
    }, 10);
}

function resetGame() {
    stopTimer();
    successfulDrops = 0;
    isGameActive = false;
    document.getElementById('game-timer').textContent = '00:00';

    // Hide Modal
    const modal = document.getElementById('victory-modal');
    modal.classList.remove('visible');
    setTimeout(() => {
        modal.style.display = 'none';
    }, 500); // Wait for transition

    // Reset Bones
    const boneYard = document.getElementById('bone-yard');
    // Ensure we preserve the original order: skull, ribcage, pelvis, left-arm, right-arm, legs
    const order = ['bone-skull', 'bone-ribcage', 'bone-pelvis', 'bone-left-arm', 'bone-right-arm', 'bone-legs'];

    order.forEach(id => {
        const bone = document.getElementById(id);
        if (bone) {
            // Remove placed class
            bone.classList.remove('placed-bone');

            // Reset styles
            bone.style.position = '';
            bone.style.left = '';
            bone.style.top = '';
            bone.style.width = '';
            bone.style.height = '';
            bone.style.margin = '';
            bone.style.transform = '';
            bone.style.zIndex = '';

            // Remove data attributes
            bone.removeAttribute('data-x');
            bone.removeAttribute('data-y');
            bone.removeAttribute('data-placeholder-id');

            // Move back to bone yard if not already there
            if (bone.parentNode !== boneYard) {
                boneYard.appendChild(bone);
            }
        }
    });
}
