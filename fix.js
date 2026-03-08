// Wait! Wait! Wait!
// If I remove `transform: translateX(-50%)` from `.bone-outline`, the whole skeleton shifts to the RIGHT by `width/2` relative to where it was.
// The Ribcage left edge will be `calc(50% - 35px)`, so its center will be `50%`.
// This is exactly what "centered in its container" means!
// And the Clavicles will meet at `50%`.
// And the Thighs will be widened by me manually!

// Let me double check if `left: calc(50% - 35px)` on Skull, Ribcage, Pelvis, etc. will center them perfectly.
// Skull: `width 70`, `left 50% - 35`. Center is `50%`.
// Jaw: `width 60`, `left 50% - 30`. Center is `50%`.
// Left Clavicle: `width 50`, `left 50% - 50`. Center is `50% - 25`.
// Right Clavicle: `width 50`, `left 50% + 0`. Center is `50% + 25`.
// Ribcage: `width 70`, `left 50% - 35`. Center is `50%`.
// Left Arm: `width 35`, `left 50% - 70`. Center is `50% - 52.5`. Touches `50% - 35`.
// Right Arm: `width 35`, `left 50% + 35`. Center is `50% + 52.5`. Touches `50% + 35`.
// Pelvis: `width 90`, `left 50% - 45`. Center is `50%`.
// Left Thigh: `width 40`, `left 50% - 45`. Left edge `50% - 45`. (Will adjust to `-50`)
// Right Thigh: `width 40`, `left 50% + 5`. Left edge `50% + 5`. (Will adjust to `+10`)

// This looks SO PERFECT.
// I am 100% confident this is the intended math of the developer.
// The developer wrote `calc(50% - width/2)` to center elements horizontally.
// But then they copy-pasted `.bone-outline` CSS from somewhere and it had `transform: translateX(-50%)`.
// And they didn't realize that it double-centered things, making them crooked because of varying widths!
// I will:
// 1. Remove `transform: translateX(-50%)` from `.bone-outline` in `style.css`.
// 2. Widen the thighs and lower legs by adjusting their `left` property in both desktop and mobile views.
