public class Question {
    private String questionText;
    private String[] answerTexts;
    private int correctAnswerIndex;

    public Question(String questionText, String answer1, String answer2, String answer3, String answer4, int correctAnswerIndex) {
        this.questionText = questionText;
        this.answerTexts = new String[]{answer1, answer2, answer3, answer4};
        this.correctAnswerIndex = correctAnswerIndex;
    }

    public String getQuestionText() {
        return questionText;
    }

    public String getAnswerText(int index) {
        return answerTexts[index];
    }

    public int getCorrectAnswerIndex() {
        return correctAnswerIndex;
    }
}
