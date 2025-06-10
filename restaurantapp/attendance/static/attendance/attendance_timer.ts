// Global variables
let timer: number | undefined;
let seconds: number = 0;
let running: boolean = false;

// Format function (00:00:00)
function formatTime(secs: number): string {
    const hours: number = Math.floor(secs / 3600);
    const minutes: number = Math.floor((secs % 3600) / 60);
    const secondsLeft: number = secs % 60;

    return (
        (hours < 10 ? '0' : '') + hours + ':' +
        (minutes < 10 ? '0' : '') + minutes + ':' +
        (secondsLeft < 10 ? '0' : '') + secondsLeft
    );
}

// Update timer in HTML
function updateDisplay(): void {
    const timerDisplay = document.getElementById('timer');
    if (timerDisplay) {
        timerDisplay.textContent = formatTime(seconds);
    }
}

// Function to get Django's token CSRF 
function getCSRFToken(): string {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
    return cookieValue || '';
}

// Event to charge DOM
document.addEventListener('DOMContentLoaded', () => {
    const punchInBtn = document.getElementById('punchInBtn');
    const punchOutBtn = document.getElementById('punchOutBtn');

    // Action Punch In
    punchInBtn?.addEventListener('click', () => {
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
    punchOutBtn?.addEventListener('click', () => {
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
