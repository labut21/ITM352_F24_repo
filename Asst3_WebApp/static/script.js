// This event listener function was generating using ChatGPT with the prompt, "Create a JavaScript function to manage form submission in a quiz app, calculate score, and stop the default form submission."
to 
document.getElementById('quizForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const questions = document.querySelectorAll('.question');
    let score = 0;

    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Show score
        document.getElementById('result').classList.remove('hidden');
        document.getElementById('score').innerText = `Your score: ${data.score}`;
        
        // Process each question's answer and put feedback
        questions.forEach((question, index) => {
            const selectedAnswer = question.querySelector('input[type="radio"]:checked');
            const correctAnswer = question.dataset.correctAnswer;

            // If an answer is selected
            if (selectedAnswer) {
                const answerLabel = selectedAnswer.parentElement;
                // Show explanation if necessary
                const explanation = question.querySelector('.explanation');
                if (selectedAnswer.value === correctAnswer) {
                    answerLabel.classList.add('correct');
                    explanation.classList.remove('hidden');
                    score++;
                } else {
                    answerLabel.classList.add('incorrect');
                    explanation.classList.remove('hidden');
                }
            }
        });
    });
});