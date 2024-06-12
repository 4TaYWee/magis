package com.example.przelicznikwalut;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText kwotaDoPrzeliczenia;
    private Spinner walutaWejsciowa;
    private Spinner walutaWyjsciowa;
    private TextView kwotaWyliczona;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        kwotaDoPrzeliczenia = findViewById(R.id.kwotaDoPrzeliczenia);
        walutaWejsciowa = findViewById(R.id.walutaWejsciowa);
        walutaWyjsciowa = findViewById(R.id.walutaWyjsciowa);
        kwotaWyliczona = findViewById(R.id.kwotaWyliczona);
    }

    public void przeliczWalute(View view) {
        // Pobierz wartości z pól wprowadzania
        double kwota = Double.parseDouble(kwotaDoPrzeliczenia.getText().toString());
        String walutaWejsciowaStr = walutaWejsciowa.getSelectedItem().toString();
        String walutaWyjsciowaStr = walutaWyjsciowa.getSelectedItem().toString();

        // Przelicz kwotę
        double kursWaluty = pobierzKursWaluty(walutaWejsciowaStr, walutaWyjsciowaStr);
        double kwotaWyliczonaValue = kwota * kursWaluty;

        // Wyświetl wynik
        kwotaWyliczona.setText(String.format("%.2f", kwotaWyliczonaValue) + " " + walutaWyjsciowaStr);
    }

    // Zaimplementuj metodę pobierającą kurs waluty (możesz użyć API walut lub fikcyjnych kursów)
    private double pobierzKursWaluty(String walutaWejsciowaStr, String walutaWyjsciowaStr) {
        // Przykład fikcyjnych kursów walut
        if (walutaWejsciowaStr.equals("PLN") && walutaWyjsciowaStr.equals("EUR")) {
            return 0.23;
        } else if (walutaWejsciowaStr.equals("EUR") && walutaWyjsciowaStr.equals("PLN")) {
            return 4.35;
        } else {
            // Domyślny kurs 1:1
            return 1.0;
        }
    }
}
