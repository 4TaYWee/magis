package com.example.quizapp;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView questionTextView;
    private RadioGroup answerRadioGroup;
    private RadioButton answer1RadioButton;
    private RadioButton answer2RadioButton;
    private RadioButton answer3RadioButton;
    private Button submitButton;

    private int currentQuestionIndex = 0;
    private int score = 0;

    // Lista pytań i odpowiedzi
    private Question[] questions = {
            new Question("Stolica Polski to:", "Kraków", "Warszawa", "Gdańsk", "Wrocław", 1),
            new Question("Jaka jest największa planeta w Układzie Słonecznym?", "Jowisz", "Saturn", "Uran", "Neptun", 0),
            new Question("Ile jest kontynentów na Ziemi?", "6", "7", "8", "9", 4),
            new Question("Kto napisał powieść 'Lalka'?", "Bolesław Prus", "Adam Mickiewicz", Henryk Sienkiewicz, Eliza Orzeszkowa, 0),
            new Question("Który pierwiastek chemiczny ma symbol Au?", "Srebro", "Złoto", "Miedź", "Platyna", 1)
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        questionTextView = findViewById(R.id.questionTextView);
        answerRadioGroup = findViewById(R.id.answerRadioGroup);
        answer1RadioButton = findViewById(R.id.answer1RadioButton);
        answer2RadioButton = findViewById(R.id.answer2RadioButton);
        answer3RadioButton = findViewById(R.id.answer3RadioButton);
        submitButton = findViewById(R.id.submitButton);

        // Ustawianie pierwszego pytania
        displayQuestion(currentQuestionIndex);

        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int selectedAnswer = getSelectedAnswer();

                // Sprawdź, czy odpowiedź jest poprawna
                if (selectedAnswer == questions[currentQuestionIndex].getCorrectAnswerIndex()) {
                    score++;
                }

                // Przejdź do następnego pytania
                currentQuestionIndex++;
                if (currentQuestionIndex < questions.length) {
                    displayQuestion(currentQuestionIndex);
                } else {
                    // Wyświetl wynik quizu
                    displayScore();
                }
            }
        });
    }

    private void displayQuestion(int index) {
        questionTextView.setText(questions[index].getQuestionText());
        answer1RadioButton.setText(questions[index].getAnswerText(0));
        answer2RadioButton.setText(questions[index].getAnswerText(1));
        answer3RadioButton.setText(questions[index].getAnswerText(2));
    }

    private int getSelectedAnswer() {
        RadioButton selectedRadioButton = findViewById(answerRadioGroup.getCheckedRadioButtonId());
        return answerRadioGroup.indexOfChild(selectedRadioButton);
    }

    private void displayScore() {
        String scoreMessage = "Twój wynik to: " + score + "/" + questions.length;
        questionTextView.setText(scoreMessage);
        answerRadioGroup.setVisibility(View.GONE);
        submitButton.setVisibility(View.GONE);
    }
}
