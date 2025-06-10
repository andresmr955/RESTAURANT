"use strict";
// Global variables
let timer;
let seconds = 0;
let running = false;
// Format function (00:00:00)
function formatTime(secs) {
    const hours = Math.floor(secs / 3600);
    const minutes = Math.floor((secs % 3600) / 60);
    const secondsLeft = secs % 60;
    return ((hours < 10 ? '0' : '') + hours + ':' +
        (minutes < 10 ? '0' : '') + minutes + ':' +
        (secondsLeft < 10 ? '0' : '') + secondsLeft);
}
// Update timer in HTML
function updateDisplay() {
    const timerDisplay = document.getElementById('timer');
    if (timerDisplay) {
        timerDisplay.textContent = formatTime(seconds);
    }
}
// Function to get Django's token CSRF 
function getCSRFToken() {
    var _a;
    const cookieValue = (_a = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))) === null || _a === void 0 ? void 0 : _a.split('=')[1];
    return cookieValue || '';
}
// Event to charge DOM
document.addEventListener('DOMContentLoaded', () => {
    const punchInBtn = document.getElementById('punchInBtn');
    const punchOutBtn = document.getElementById('punchOutBtn');
    // Action Punch In
    punchInBtn === null || punchInBtn === void 0 ? void 0 : punchInBtn.addEventListener('click', () => {
        if (!running) {
            running = true;
            timer = window.setInterval(() => {
                seconds++;
                updateDisplay();
            }, 1000);
            // Call Ajax to register time
            fetch('/attendance/start/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({})
            })
                .then(response => response.json())
                .then(data => {
                console.log('Punch In registered:', data);
            })
                .catch(error => {
                console.error('Error al make Punch In:', error);
            });
        }
    });
    // Action Punch Out
    punchOutBtn === null || punchOutBtn === void 0 ? void 0 : punchOutBtn.addEventListener('click', () => {
        if (running) {
            running = false;
            clearInterval(timer);
            // Call AJAX to register punch out
            fetch('/attendance/stop/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    elapsed_seconds: seconds
                })
            })
                .then(response => response.json())
                .then(data => {
                console.log('Punch Out registered:', data);
            })
                .catch(error => {
                console.error('Error to Punch Out:', error);
            });
        }
    });
    updateDisplay();
});
