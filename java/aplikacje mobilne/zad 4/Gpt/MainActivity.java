import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private TextView questionTextView;
    private RadioGroup optionsRadioGroup;
    private Button submitButton;

    // Array to hold questions and their respective correct answers
    private String[] questions = {"Question 1?", "Question 2?", "Question 3?"};
    private String[] correctAnswers = {"Correct Option 1", "Correct Option 2", "Correct Option 3"};

    private int currentQuestionIndex = 0;
    private int score = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        questionTextView = findViewById(R.id.questionTextView);
        optionsRadioGroup = findViewById(R.id.optionsRadioGroup);
        submitButton = findViewById(R.id.submitButton);

        displayQuestion();

        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkAnswer();
            }
        });
    }

    private void displayQuestion() {
        questionTextView.setText(questions[currentQuestionIndex]);
        // Assuming you have only two options, you can adjust accordingly
        ((RadioButton) optionsRadioGroup.getChildAt(0)).setText("Option 1");
        ((RadioButton) optionsRadioGroup.getChildAt(1)).setText("Option 2");
        // Set other options accordingly
    }

    private void checkAnswer() {
        int selectedOptionId = optionsRadioGroup.getCheckedRadioButtonId();
        if (selectedOptionId != -1) {
            RadioButton selectedRadioButton = findViewById(selectedOptionId);
            String selectedAnswer = selectedRadioButton.getText().toString();
            if (selectedAnswer.equals(correctAnswers[currentQuestionIndex])) {
                score++;
            }
            if (currentQuestionIndex < questions.length - 1) {
                currentQuestionIndex++;
                displayQuestion();
                optionsRadioGroup.clearCheck();
            } else {
                endQuiz();
            }
        } else {
            Toast.makeText(this, "Please select an option", Toast.LENGTH_SHORT).show();
        }
    }

    private void endQuiz() {
        // Display the score or any other end of quiz actions
        Toast.makeText(this, "Quiz ended. Your score: " + score, Toast.LENGTH_SHORT).show();
        // You can add more actions like displaying the score in a TextView or saving it, etc.
    }
}
