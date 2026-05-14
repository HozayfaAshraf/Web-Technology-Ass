// Close alert/message boxes
function closeMessageBox(overlayId, boxId) {
    const overlay = document.getElementById(overlayId);
    const box = document.getElementById(boxId);

    if (overlay) {
        overlay.style.display = 'none';
    }

    if (box) {
        box.style.display = 'none';
    }
}

window.closeMessageBox = closeMessageBox;

// Delegated click handler: works regardless of script load order
document.addEventListener('click', function (e) {

    const btn = e.target.closest('.btn-close, .btn-complete');
    if (!btn) return;

    //find the alert box container (either #alert-box or #alert-box-success)
    const box = btn.closest('#alert-box, #alert-box-success');
    if (!box) return;

    const overlayId = box.id === 'alert-box' ? 'alert-overlay' : 'alert-overlay-success';
    closeMessageBox(overlayId, box.id);
});
