/*
  This script powers the mobile menu and the copy-to-clipboard functionality.
*/

document.addEventListener('DOMContentLoaded', () => {
    // --- MOBILE MENU LOGIC (Runs on all pages) ---
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
    const closeMenuBtn = document.getElementById('close-menu-btn');

    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', () => {
            mobileMenuOverlay.classList.add('is-open');
        });
    }

    if (closeMenuBtn) {
        closeMenuBtn.addEventListener('click', () => {
            mobileMenuOverlay.classList.remove('is-open');
        });
    }

    // --- COPY TO CLIPBOARD LOGIC (Onboarding page) ---
    const copyButton = document.getElementById('copy-button');
    const questionnaireText = document.getElementById('questionnaire-text');

    if (copyButton && questionnaireText) {
        copyButton.addEventListener('click', () => {
            navigator.clipboard.writeText(questionnaireText.innerText).then(() => {
                copyButton.textContent = 'Copied!';
                setTimeout(() => {
                    copyButton.textContent = 'Copy Questionnaire';
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy text: ', err);
            });
        });
    }
});

