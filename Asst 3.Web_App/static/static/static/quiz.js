document.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch('/api/questions');
    const questions = await response.json();
    let currentQuestionIndex = 0;

    function displayQuestion() {
        const question = questions[currentQuestionIndex];
        document.getElementById('question').textContent = question.question;
        const optionsContainer = document.getElementById('options');
        optionsContainer.innerHTML = '';

        question.options.forEach((option, index) => {
            const optionDiv = document.createElement('div');
            optionDiv.className = 'option';
            optionDiv.textContent = option;
            optionDiv.dataset.answer = option[0].toLowerCase();
            optionDiv.onclick = () => checkAnswer(optionDiv, question.answer, question.explanation);
            optionsContainer.appendChild(optionDiv);
        });
    }

    function checkAnswer(selectedOption, correctAnswer, explanationText) {
        const options = document.querySelectorAll('.option');
        options.forEach(option => option.classList.remove('correct-answer', 'incorrect-answer'));

        if (selectedOption.dataset.answer === correctAnswer) {
            selectedOption.classList.add('correct-answer');
        } else {
            selectedOption.classList.add('incorrect-answer');
            const explanation = document.getElementById('explanation');
            explanation.textContent = explanationText;
            explanation.style.opacity = 1;
        }
    }

    displayQuestion();
});