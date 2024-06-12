package com.example.calendarapp.ui.activities;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import androidx.appcompat.app.AppCompatActivity;
import com.example.calendarapp.R;

public class MainActivity extends AppCompatActivity {

    private Button dailyViewButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dailyViewButton = findViewById(R.id.button_daily_view);
        dailyViewButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Przejście do widoku dziennego
                Intent intent = new Intent(MainActivity.this, DailyViewActivity.class);
                startActivity(intent);
            }
        });
    }
}
